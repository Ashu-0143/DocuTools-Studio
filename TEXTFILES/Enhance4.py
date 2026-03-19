import cv2
import numpy as np
import os
import shutil
import re
import gc  # Garbage Collector to fix memory issues
from pathlib import Path
from PIL import Image
import pillow_heif
import fitz  # PyMuPDF

pillow_heif.register_heif_opener()

class StudioProProcessor:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.backup_path = self.base_path / "originals"
        self.backup_path.mkdir(exist_ok=True)
        self.valid_exts = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp', '.pdf'}

    def get_info(self, filename):
        name, ext = os.path.splitext(filename)
        match = re.search(r'^(.*)_e(\d+)$', name)
        if match:
            return match.group(1), int(match.group(2)), ext
        return name, 0, ext

    def adjust_lighting(self, img, mode):
        # Ensure image is in 8-bit format to save memory
        if img.dtype != np.uint8:
            img = cv2.convertScaleAbs(img)
            
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        if mode == '1': # Fair
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            l = clahe.apply(l)
            img = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)
            return cv2.convertScaleAbs(img, alpha=1.1, beta=5)
        elif mode == '2': # Light
            l = cv2.add(l, 25)
        elif mode == '3': # Dark
            l = cv2.subtract(l, 25)
            
        return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

    def undo(self):
        files = [f for f in self.base_path.iterdir() if f.suffix.lower() in self.valid_exts]
        undone_count = 0
        for file_path in files:
            base, version, ext = self.get_info(file_path.name)
            if version == 0: continue 
            
            prev_v = version - 1
            search = f"{base}_e{prev_v}{ext}" if prev_v > 0 else f"{base}{ext}"
            backup_source = self.backup_path / search

            if backup_source.exists():
                file_path.unlink()
                shutil.copy(str(backup_source), str(self.base_path / search))
                undone_count += 1
        print(f"⏪ Reverted {undone_count} files.")
        gc.collect() # Clean RAM

    def run(self, mode):
        # Get list first to avoid processing files created during this run
        files = [f for f in self.base_path.iterdir() if f.suffix.lower() in self.valid_exts]
        processed = 0

        for file_path in files:
            if file_path.name == Path(__file__).name: continue
            
            try:
                # 1. Backup current state
                shutil.copy(str(file_path), str(self.backup_path / file_path.name))
                
                base, version, ext = self.get_info(file_path.name)
                new_name = f"{base}_e{version + 1}{ext}"
                
                # 2. Process
                if ext == '.pdf':
                    doc = fitz.open(file_path)
                    for i, page in enumerate(doc):
                        pix = page.get_pixmap(dpi=200) # Lowered DPI slightly to save RAM
                        img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
                        cv_img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR) if pix.n == 3 else img_data
                        res = self.adjust_lighting(cv_img, mode)
                        cv2.imwrite(str(self.base_path / f"{base}_e{version+1}_pg{i+1}.jpg"), res)
                    doc.close()
                else:
                    # Open and immediately close PIL handle to save memory
                    with Image.open(file_path) as pil_img:
                        cv_img = cv2.cvtColor(np.array(pil_img.convert('RGB')), cv2.COLOR_RGB2BGR)
                    
                    enhanced = self.adjust_lighting(cv_img, mode)
                    cv2.imwrite(str(self.base_path / new_name), enhanced)
                
                # 3. Clean up
                file_path.unlink()
                print(f"✅ Created: {new_name}")
                processed += 1
                
                # Clear memory for this specific image
                del cv_img
                gc.collect() 

            except Exception as e:
                print(f"❌ Error on {file_path.name}: {e}")

if __name__ == "__main__":
    proc = StudioProProcessor()
    while True:
        print("\n--- STUDIO PRO (MEMORY SAFE) ---")
        print("1. Fair | 2. Light | 3. Dark | 4. UNDO | 5. EXIT")
        c = input("Choice: ")
        if c in ['1', '2', '3']: proc.run(c)
        elif c == '4': proc.undo()
        elif c == '5': break
