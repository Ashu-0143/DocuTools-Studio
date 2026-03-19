# 📄 toWORD Tool

Convert **Images & PDF → Word (.docx)** automatically.

---

## 🚀 What it does

* Converts:

  * **Images → Word (.docx)**
  * **PDF → Word (.docx)**
* Keeps output in same folder
* Moves original files to `temp/`
* Simple bulk processing

---

## 📁 Folder Structure

```
_toWORD/
│   toWORD.py
│   temp/
```

---

## ⚙️ Requirements

Install required libraries:

```
pip install python-docx pdf2docx
```

---

## ▶️ How to Use

1. Put files inside `_toWORD` folder:

   * Images (jpg, png, webp, etc.)
   * PDF files

2. Run:

```
python toWORD.py
```

3. Done ✅

   * `.docx` files will be created
   * Originals moved to `temp/`

---

## 🧠 How it works

### 🖼️ Images → Word

* Creates a Word document
* Sets **A4 page size**
* Inserts image centered
* Scales image to fit nicely

Example:

```
photo.jpg → photo.docx
```

---

### 📄 PDF → Word

* Converts full PDF → editable Word file

Example:

```
file.pdf → file.docx
```

---

## 📌 Notes

* Supports:

  * Images: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp`
  * PDF files
* Each file → separate Word document
* Keeps filenames same

---

## 💡 Example

Input:

```
image.png
doc.pdf
```

Output:

```
image.docx
doc.docx
```

---

## 🧹 Cleanup

* Originals moved to:

```
temp/
```

---

## ⚠️ Common Issues

### ❗ Font Problems (PDF → Word)

* Fonts may change or break
* Some text may appear different
  → This is normal (PDF → editable format issue)

---

### ❗ Layout Issues

* Complex PDFs (tables, columns, designs) may not convert perfectly

---

### ❗ Image Quality

* Very large images may be resized
* Some clarity loss possible

---

### ❗ Conversion Errors

* Corrupted PDF → may fail
* Unsupported image → skipped

---

## ✨ Simple Image + PDF → Word converter
