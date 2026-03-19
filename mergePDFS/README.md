# 📄 Merge PDFs with Blank Pages

---

## 📌 Overview
This script:
- Merges multiple **PDF files into one**
- Automatically adds **blank pages** if needed
- Ensures proper **front-back printing alignment**
- Moves original PDFs to `temp`

---

## 📂 Folder Structure
```
Merge PDF with blanks/
│   merge pdfs.py
│
└───temp
    (merged files moved here)
```

---

## ⚙️ Requirements
```bash
pip install pypdf
```

---

## 🚀 How To Use
1. Place all **PDF files** in the folder  
2. Run:
```bash
python "merge pdfs.py"
```

3. Output:
```
Final_Merged_Document.pdf
```

4. Original PDFs → moved to:
```
temp/
```

---

## 🧠 Key Logic

### 📚 Merging
```python
writer.append(reader)
```
- Combines all PDFs in sorted order

---

### 📄 Blank Page Logic
```python
if num_pages % 2 != 0:
    writer.add_blank_page()
```
- If a PDF has **odd pages**
- Adds **1 blank page**
- Ensures proper **duplex (front/back) printing**

---

### 🧹 Cleanup
- After merging:
  - All original PDFs moved to `temp`
  - Prevents duplicate processing

---

## ⚡ Features
- ✔️ Batch PDF merging
- ✔️ Auto blank page insertion
- ✔️ Print-ready output
- ✔️ Clean folder management
- ✔️ Auto overwrite temp files

---

## ⚠️ Limitations
- Only works with **PDF files**
- Order depends on **filename sorting**

---

## 💡 Tips
- Rename files like:
```
1.pdf, 2.pdf, 3.pdf
```
for correct order

- Useful for:
  - Booklets
  - ID card prints
  - Duplex printing

---

## 🧾 Output
- Final file:
```
Final_Merged_Document.pdf
```

---
