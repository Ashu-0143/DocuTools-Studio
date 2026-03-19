# 📄 DocuTools-Studio

A clean collection of Python tools to handle **documents, ID cards, PDFs, and images** in a fast, practical way.

---

## ✨ What you can do

### 🪪 ID Card Processing

* Aadhar
* PAN
* Voter ID
* RC (Registration Certificate)
* Senior Citizenship

✔ Extract front & back automatically
✔ Works with password-protected PDFs
✔ Clean output with proper naming

---

### 🖼️ Image Tools

* ✂️ Auto crop white borders
* 🎨 Enhance images (light / dark / balanced)
* 🧾 Passport photo sheet generator

---

### 📄 PDF & Conversion Tools

* 📚 Merge PDFs (with blank page support)
* 🔄 Convert files:

  * PDF → JPG
  * JPG → PDF
  * PDF/Image → Word

---

## 📁 Project Structure

```
AADHAR/
PAN/
VOTER/
RC/
SENIOR CITIZENSHIP/
cropBorder/
Enhance/
mergePDFS/
Passphoto Maker/
_toJPG/
_toPDF/
_toWORD/
```

---

## ⚙️ Setup

Install all dependencies:

```
pip install opencv-python numpy pillow pdf2image pypdf docx2pdf python-docx pdf2docx pymupdf pillow-heif
```

---

## ▶️ Usage

Run any tool directly:

```
python script_name.py
```

Example:

```
cd AADHAR
python Aadhar.py
```

---

## ⚠️ Important Notes

* Update **POPPLER path** inside scripts (for PDF tools)
* Designed mainly for **Windows**
* Input files → same folder as script
* Output → `output/` folder (or same directory)
* Originals → moved to `temp/`

---

## 🔥 Why this project

* Built for **real-world usage** (shops, document work, etc.)
* Handles bulk files easily
* Supports multiple formats
* Simple folder-based workflow (no complex setup)

---

## 📬 Support / Suggestions

Found an issue? Have an idea to improve this?

📧 **Email:** [ashok8755.p@gmail.com](mailto:ashok8755.p@gmail.com)
💬 Or open an issue on GitHub

---

## 👤 Author

GitHub: https://github.com/Ashu-0143

---
