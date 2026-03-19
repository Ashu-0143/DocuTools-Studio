import os
import shutil
from pathlib import Path
from PIL import Image, ImageOps

def create_rotated_passport_sheet_with_border():
    CURRENT_DIR = Path.cwd()
    TEMP_DIR = CURRENT_DIR / "temp"
    TEMP_DIR.mkdir(exist_ok=True)

    # 700 DPI Settings
    DPI = 700
    SHEET_W, SHEET_H = int(4 * DPI), int(6 * DPI) # 2800x4200
    
    # 45mm wide x 35mm high
    PHOTO_W, PHOTO_H = int(45 * DPI / 25.4), int(35 * DPI / 25.4)
    BORDER_PX = 3  # 3-pixel black stroke
    
    # Grid: 2 columns, 4 rows
    COLS, ROWS = 2, 4
    
    # Calculate spacing (including the border thickness in the photo size)
    TOTAL_PHOTO_W = PHOTO_W + (BORDER_PX * 2)
    TOTAL_PHOTO_H = PHOTO_H + (BORDER_PX * 2)
    
    GAP_X = (SHEET_W - (COLS * TOTAL_PHOTO_W)) // (COLS + 1)
    GAP_Y = (SHEET_H - (ROWS * TOTAL_PHOTO_H)) // (ROWS + 1)

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    image_files = [f for f in CURRENT_DIR.iterdir() if f.suffix.lower() in valid_extensions]

    if not image_files:
        print("No images found in the directory.")
        return

    for img_path in image_files:
        try:
            print(f"Processing: {img_path.name}")
            
            with Image.open(img_path) as img:
                img_rgb = img.convert("RGB")
                
                # Resize to portrait first (35x45mm)
                temp_w, temp_h = int(35 * DPI / 25.4), int(45 * DPI / 25.4)
                resized = img_rgb.resize((temp_w, temp_h), Image.Resampling.LANCZOS)
                
                # Rotate 90 degrees to make it landscape (45x35mm)
                passport_photo = resized.transpose(Image.ROTATE_90)
                
                # --- ADD BLACK STROKE ---
                passport_photo = ImageOps.expand(passport_photo, border=BORDER_PX, fill='black')
            
            # Create blank 4x6 canvas
            canvas = Image.new('RGB', (SHEET_W, SHEET_H), 'white')
            
            # Paste the 8 bordered pieces
            for row in range(ROWS):
                for col in range(COLS):
                    x = GAP_X + col * (TOTAL_PHOTO_W + GAP_X)
                    y = GAP_Y + row * (TOTAL_PHOTO_H + GAP_Y)
                    canvas.paste(passport_photo, (x, y))
            
            # Save and clean up
            output_name = f"Sheet_{img_path.name}"
            canvas.save(output_name, "JPEG", quality=98, dpi=(DPI, DPI))
            
            shutil.move(str(img_path), str(TEMP_DIR / img_path.name))
            os.rename(output_name, img_path.name)
            
            print(f"Successfully created sheet for {img_path.name}")

        except Exception as e:
            print(f"Error processing {img_path.name}: {e}")

    print("\nAll files processed! Originals moved to 'temp'.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    create_rotated_passport_sheet_with_border()
