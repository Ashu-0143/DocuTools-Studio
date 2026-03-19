# 📄 toJPG Tool

Convert **PDF, Word, and Images → JPG** automatically.

---

## 🚀 What it does

* Converts:

  * **PDF → JPG (each page)**
  * **Word (.doc/.docx) → JPG**
  * **Images → JPG**
* Keeps output in same folder
* Moves original files to `temp/` (to keep things clean)
* Handles **password-protected PDFs**
* Maintains **high quality (300 DPI)**

---

## 📁 Folder Structure

```
_toJPG/
│   toJPG.py
│   temp/
```

---

## ⚙️ Requirements

Install required libraries:

```
pip install pillow pdf2image docx2pdf
```

### 🔹 Poppler (IMPORTANT for PDF)

* Download Poppler for Windows
* Extract it
* Update this path inside code:

```python
POPPLER = r'YOUR_PATH_TO_POPPLER\Library\bin'
```

---

## ▶️ How to Use

1. Copy files into `_toJPG` folder:

   * PDF / DOCX / Images
2. Run:

```
python toJPG.py
```

3. Done ✅

   * JPG files will be created
   * Originals moved to `temp/`

---

## 🧠 How it works

### 📄 PDF

* Converts each page → separate JPG
* Example:

```
file.pdf → file_1.jpg, file_2.jpg
```

### 📝 Word Files

* Converts Word → PDF → JPG

### 🖼️ Images

* Converts formats like:

  * PNG, WEBP, JPEG, HEIF → JPG
* Fixes transparency (adds white background)

---

## 📌 Notes

* `.jpg` files are not duplicated
* Password asked only if needed for PDF
* Errors are skipped (won’t stop whole process)

---

## 💡 Example

Input:

```
sample.pdf
photo.png
doc.docx
```

Output:

```
sample_1.jpg
sample_2.jpg
photo.jpg
doc_1.jpg
```

---

## 🧹 Cleanup

* All original files moved to:

```
temp/
```

---

## ⚠️ Common Issues

* **PDF not converting?**
  → Check Poppler path

* **Word not converting?**
  → Make sure MS Word is installed

---

## ✨ Simple & fast bulk conversion tool
