# 📄 toPDF Tool

Convert **Images & Word → PDF** with backup support.

---

## 🚀 What it does

* Converts:

  * **JPG/JPEG → PDF**
  * **Word (.docx) → PDF**
* Option to:

  * Merge all images → **one PDF**
  * Convert each image → **separate PDFs**
* Automatically creates a **backup ZIP**
* Deletes originals after processing

---

## 📁 Folder Structure

```
_toPDF/
│   toPDF.py
│   temp/
```

---

## ⚙️ Requirements

Install required libraries:

```
pip install pillow docx2pdf
```

---

## ▶️ How to Use

1. Put files inside `_toPDF` folder:

   * Images (.jpg / .jpeg)
   * Word files (.docx)

2. Run:

```
python toPDF.py
```

3. Choose mode:

```
1 → Merge all images into one PDF
2 → Convert each image separately
```

4. Done ✅

---

## 🧠 How it works

### 🖼️ Images → PDF

* Converts all images to RGB
* Two modes:

#### 🔹 Mode 1 (Merge)

```
img1.jpg + img2.jpg → merged_images.pdf
```

#### 🔹 Mode 2 (Separate)

```
img1.jpg → img1.pdf
img2.jpg → img2.pdf
```

---

### 📝 Word → PDF

* Converts `.docx` → `.pdf`
* Uses MS Word internally

---

### 📦 Backup System

* All original files are zipped:

```
temp/files_backup.zip
```

* Then originals are removed from main folder

---

## 📌 Notes

* Works only with:

  * `.jpg`, `.jpeg`, `.docx`
* Skips other file types
* Memory cleaned after processing (for large files)

---

## 💡 Example

Input:

```
a.jpg
b.jpg
doc.docx
```

Output (Mode 1):

```
merged_images.pdf
doc.pdf
```

Backup:

```
temp/files_backup.zip
```

---

## ⚠️ Common Issues

* **Word not converting?**
  → Make sure MS Word is installed

* **No output?**
  → Check if files are correct format

---

## 🧹 Cleanup

* Originals removed after process
* Backup available in:

```
temp/files_backup.zip
```

---

## ✨ Simple bulk Image + Word → PDF converter
