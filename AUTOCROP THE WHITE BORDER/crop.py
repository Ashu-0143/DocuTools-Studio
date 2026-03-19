import os
from PIL import Image, ImageChops
from pdf2image import convert_from_path

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE, 'Cropped_Results')
POPPLER = r'C:\Users\rao\Documents\work\poppler-25.12.0\Library\bin'

os.makedirs(OUTPUT, exist_ok=True)

def trim_white_border(img):
    img = img.convert('RGB')
    bg = Image.new('RGB', img.size, (255, 255, 255))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    return img.crop(bbox) if bbox else img

def process_cropping():
    this_script = os.path.basename(__file__)
    items = [f for f in os.listdir(BASE) if os.path.isfile(os.path.join(BASE, f)) and f != this_script]
    
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
    print(f"\nDone! Results in: {OUTPUT}")
