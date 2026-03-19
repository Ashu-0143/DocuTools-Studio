import os
import shutil
from pypdf import PdfWriter, PdfReader

# Setup paths relative to where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")
OUTPUT_NAME = "Final_Merged_Document.pdf"

def merge_and_cleanup():
    # 1. Create temp folder if it doesn't exist
    os.makedirs(TEMP_DIR, exist_ok=True)
    
    writer = PdfWriter()
    
    # 2. Get and sort all PDF files (excluding the output and script itself)
    pdf_files = [f for f in sorted(os.listdir(BASE_DIR)) 
                 if f.lower().endswith('.pdf') and f != OUTPUT_NAME]
    
    if not pdf_files:
        print("No PDF files found to merge.")
        return

    print(f"Starting merge of {len(pdf_files)} files...")

    for filename in pdf_files:
        filepath = os.path.join(BASE_DIR, filename)
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        
        # Add the PDF to our final document
        writer.append(reader)
        
        # 3. Add blank page if page count is odd
        if num_pages % 2 != 0:
            print(f"  + Added blank page to '{filename}' (was {num_pages} pgs)")
            writer.add_blank_page()
        else:
            print(f"  - Added '{filename}' ({num_pages} pgs)")

    # 4. Save the final merged PDF
    output_path = os.path.join(BASE_DIR, OUTPUT_NAME)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    writer.close()

    # 5. Move original files to temp folder
    for filename in pdf_files:
        src = os.path.join(BASE_DIR, filename)
        dst = os.path.join(TEMP_DIR, filename)
        
        # Handle filename conflicts in temp (if you run this multiple times)
        if os.path.exists(dst):
            os.remove(dst) 
            
        shutil.move(src, dst)

    print(f"\nDone! Merged PDF: {OUTPUT_NAME}")
    print(f"Originals moved to: {TEMP_DIR}")

if __name__ == "__main__":
    merge_and_cleanup()
