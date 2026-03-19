# 📄 DocuTools-Studio

🚀 A powerful collection of Python tools for automating document processing in real-world workflows (ID cards, PDFs, images).

---

## ✨ Features

### 🪪 ID Card Processing

* Aadhar Card
* PAN Card
* Voter ID
* RC (Registration Certificate)
* Senior Citizenship

✔ Extract front & back automatically
✔ Handles password-protected PDFs
✔ Auto file indexing

---

### 🖼️ Image Tools

* ✂️ Auto crop white borders
* 🎨 Image enhancement (Fair / Light / Dark)
* 🧾 Passport photo sheet generator (4x6)

---

### 📄 PDF Tools

* 📚 Merge PDFs (auto blank page support)
* 🔄 Convert:

  * PDF → JPG
  * JPG → PDF
  * PDF/Image → Word

---

## 📁 Project Structure

```bash
AADHAR/
PAN/
VOTER/
RC/
SENIOR CITIZENSHIP/
AUTOCROP THE WHITE BORDER/
Enhance/
Merge PDF with blanks/
Passphoto Maker/
```

---

## ⚙️ Setup

```bash
pip install opencv-python numpy pillow pdf2image pypdf docx2pdf python-docx pdf2docx pymupdf pillow-heif
```

---

## ▶️ Usage

Run any script:

```bash
python script_name.py
```

Example:

```bash
cd AADHAR
python Aadhar.py
```

---

## ⚠️ Important Notes

* Update `POPPLER_PATH` inside scripts
* Designed for Windows
* Input files → same folder
* Output → `output/`
* Originals → `temp/`

---

## 🔥 Highlights

* Real-world studio automation
* Batch processing support
* Handles multiple file formats
* Clean folder-based workflow

---

## 👤 Author

GitHub: https://github.com/Ashu-0143
