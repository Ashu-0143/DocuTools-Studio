import os
import shutil
from PIL import Image
from pdf2image import convert_from_path
from docx2pdf import convert as docx_to_pdf

BASE = os.path.dirname(os.path.abspath(__file__))
TEMP = os.path.join(BASE, 'temp')
POPPLER = r'C:\Users\rao\Documents\work\poppler-25.12.0\Library\bin'

os.makedirs(TEMP, exist_ok=True)

def process_files():
    for file in os.listdir(BASE):
        src = os.path.join(BASE, file)
        if os.path.isdir(src) or file.lower().endswith('.py') or file == 'temp':
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()
        
        try:
            if ext in ['.doc', '.docx']:
                temp_pdf = os.path.join(TEMP, f"{name}_temp.pdf")
                docx_to_pdf(src, temp_pdf)
                pages = convert_from_path(temp_pdf, dpi=300, poppler_path=POPPLER)
                for i, p in enumerate(pages, 1):
                    p.save(os.path.join(BASE, f"{name}_{i}.jpg"), "JPEG", quality=95)
                shutil.move(src, os.path.join(TEMP, file))
                if os.path.exists(temp_pdf):
                    os.remove(temp_pdf)

            elif ext == '.pdf':
                try:
                    pages = convert_from_path(src, dpi=300, poppler_path=POPPLER)
                except:
                    pwd = input(f"Password for {file}: ")
                    pages = convert_from_path(src, dpi=300, poppler_path=POPPLER, userpw=pwd)
                for i, p in enumerate(pages, 1):
                    p.save(os.path.join(BASE, f"{name}_{i}.jpg"), "JPEG", quality=95)
                shutil.move(src, os.path.join(TEMP, file))

            elif ext in ['.png', '.webp', '.jpeg', '.jpg', '.heif']:
                with Image.open(src) as img:
                    if img.mode in ("RGBA", "P"):
                        bg = Image.new("RGB", img.size, (255, 255, 255))
                        bg.paste(img, mask=img.convert("RGBA").split()[3])
                        img = bg
                    else:
                        img = img.convert('RGB')
                    img.save(os.path.join(BASE, f"{name}.jpg"), "JPEG", quality=95)
                if ext != '.jpg':
                    shutil.move(src, os.path.join(TEMP, file))
        except Exception as e:
            print(f"Error {file}: {e}")

if __name__ == "__main__":
    process_files()
