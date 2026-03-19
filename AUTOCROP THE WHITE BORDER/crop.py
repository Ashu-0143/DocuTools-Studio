import os
from PIL import Image, ImageOps, ImageChops
from pdf2image import convert_from_path

# --- Configuration ---
BASE = r'C:\Users\rao\Desktop\SIRISHA STUDIO\AUTOCROP'
OUTPUT = os.path.join(BASE, 'Cropped_Results')
POPPLER = r'C:\Users\rao\Documents\work\poppler-25.12.0\Library\bin'

os.makedirs(OUTPUT, exist_ok=True)

def trim_white_border(img):
    """
    Finds the bounding box of non-white content and crops it.
    Works by inverting the image so white becomes black (0) 
    and using getbbox to find the content.
    """
    img = img.convert('RGB')
    # Use ImageChops to find difference from a solid white background
    bg = Image.new('RGB', img.size, (255, 255, 255))
    diff = ImageChops.difference(img, bg)
    
    # Add some tolerance for 'near-white' pixels (useful for scans)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)
    return img

def process_cropping():
    items = [f for f in os.listdir(BASE) if os.path.isfile(os.path.join(BASE, f))]
    
    for file in items:
        ext = os.path.splitext(file)[1].lower()
        path = os.path.join(BASE, file)
        
        try:
            if ext in ['.jpg', '.jpeg', '.png', '.webp']:
                print(f"Cropping Image: {file}")
                with Image.open(path) as img:
                    cropped = trim_white_border(img)
                    cropped.save(os.path.join(OUTPUT, f"cropped_{file}"), quality=95)

            elif ext == '.pdf':
                print(f"Cropping PDF: {file}")
                pages = convert_from_path(path, dpi=300, poppler_path=POPPLER)
                cropped_pages = [trim_white_border(p) for p in pages]
                
                if cropped_pages:
                    cropped_pages[0].save(
                        os.path.join(OUTPUT, f"cropped_{file}"),
                        save_all=True,
                        append_images=cropped_pages[1:],
                        optimize=True
                    )
        except Exception as e:
            print(f"Skipping {file}: {e}")

if __name__ == "__main__":
    process_cropping()
    print(f"\nDone! Cropped files are in: {OUTPUT}")
