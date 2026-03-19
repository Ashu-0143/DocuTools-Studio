import os
import shutil
from pypdf import PdfWriter, PdfReader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")
OUTPUT_NAME = "_Merged.pdf"

def merge_and_cleanup():
    os.makedirs(TEMP_DIR, exist_ok=True)
    writer = PdfWriter()

    pdf_files = [f for f in sorted(os.listdir(BASE_DIR)) 
                 if f.lower().endswith(".pdf") and f != OUTPUT_NAME]

    if not pdf_files:
        print("No PDF files found to merge.")
        return

    for filename in pdf_files:
        filepath = os.path.join(BASE_DIR, filename)
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        
        writer.append(reader)

        if num_pages % 2 != 0:
            writer.add_blank_page()

    output_path = os.path.join(BASE_DIR, OUTPUT_NAME)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    
    writer.close()

    for filename in pdf_files:
        src = os.path.join(BASE_DIR, filename)
        dst = os.path.join(TEMP_DIR, filename)
        
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(src, dst)

    print(f"Merged {len(pdf_files)} files into {OUTPUT_NAME}")

if __name__ == "__main__":
    merge_and_cleanup()
