import os
import cv2
import numpy as np
from pdf2image import convert_from_path
import shutil
import re
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POPPLER_PATH = r"C:\Users\rao\Documents\work\poppler-25.12.0\Library\bin"
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMP_DIR = os.path.join(BASE_DIR, "temp")
VALID_EXTENSIONS = ('.pdf', '.jpg', '.jpeg')

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

def get_next_index(directory):
    existing_files = os.listdir(directory)
    max_num = 0
    for f in existing_files:
        match = re.match(r"^(\d+)", f)
        if match:
            num = int(match.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1

def move_to_temp_safely(source_path, temp_dir):
    original_filename = Path(source_path).name
    destination_path = Path(temp_dir) / original_filename
    counter = 1
    while destination_path.exists():
        new_filename = f"{Path(source_path).stem}_{counter}{Path(source_path).suffix}"
        destination_path = Path(temp_dir) / new_filename
        counter += 1
    shutil.move(source_path, destination_path)
    print(f"  Moved original to temp folder: {destination_path.name}")

def process_aadhar_files():
    script_name = os.path.basename(__file__)
    files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f)) 
             and Path(f).suffix.lower() in VALID_EXTENSIONS 
             and f != script_name]
    
    if not files:
        print(f"No files found in {BASE_DIR}")
        return

    card_index = get_next_index(OUTPUT_DIR)
    
    for filename in files:
        input_path = os.path.join(BASE_DIR, filename)
        file_extension = Path(filename).suffix.lower()
        file_stem = Path(filename).stem
        image_to_process_path = input_path
        temp_jpg_path = None
        
        print(f"\nProcessing: {filename}")

        try:
            if file_extension == '.pdf':
                if len(file_stem) == 8:
                    password = file_stem
                    print(f"  Using filename as password: {password}")
                else:
                    password = input("    Enter Password (8 characters): ").strip()
                
                pages = []
                try:
                    pages = convert_from_path(input_path, dpi=700, poppler_path=POPPLER_PATH, userpw=password)
                except:
                    pass
                
                if not pages:
                    print(f"  *Failed to extract pages. Check password.*")
                    continue
                
                temp_jpg_name = f"temp_{file_stem}.jpg"
                temp_jpg_path = os.path.join(BASE_DIR, temp_jpg_name)
                pages[0].save(temp_jpg_path, 'JPEG', quality=95)
                image_to_process_path = temp_jpg_path
            
            full_page = cv2.imread(image_to_process_path) 
            
            if full_page is None or full_page.size == 0:
                print(f"  *Failed to load image: {Path(image_to_process_path).name}*")
                continue

            front_card = full_page[5565:7128, 478:2928] 
            back_card = full_page[5570:7128, 3031:5476] 

            if front_card.size == 0 or back_card.size == 0:
                print(f"  *Error: Cropped area empty.*")
                if temp_jpg_path and os.path.exists(temp_jpg_path):
                    os.remove(temp_jpg_path)
                continue

            front_name = f"{card_index}f.jpg"
            back_name = f"{card_index}b.jpg"
            
            cv2.imwrite(os.path.join(OUTPUT_DIR, front_name), front_card, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            cv2.imwrite(os.path.join(OUTPUT_DIR, back_name), back_card, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
            print(f"  Saved: {front_name} and {back_name}")

            move_to_temp_safely(input_path, TEMP_DIR)
            
            if temp_jpg_path and os.path.exists(temp_jpg_path):
                os.remove(temp_jpg_path)

            card_index += 1

        except Exception as e:
            print(f"  *Error: {e}*")
            if temp_jpg_path and os.path.exists(temp_jpg_path):
                os.remove(temp_jpg_path)

if __name__ == "__main__":
    process_aadhar_files()
    print(f"\nTask complete.")
