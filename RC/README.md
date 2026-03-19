# 🚗 RC Card Processor

> ⚠️ **Note:** Sample image used here is a **PAN card**, but the script is designed **only for RC (Registration Certificate) Cards**.

---

## 📌 Overview
This script:
- Takes **RC Card PDF**
- Extracts **Front & Back pages**
- Enhances image quality
- Saves as **high-quality JPGs**
- Moves processed files to `temp`

---

## 📂 Folder Structure
```
RC/
│   RC.py
│   RC card pdf.pdf
│
├───output
│   │   1f.jpg
│   │   1b.jpg
│
└───temp
```

---

## 🖼️ Sample Output
![Sample](../assets/sample1.jpg)

---

## ⚙️ Requirements
```bash
pip install opencv-python numpy pdf2image
```

Install **Poppler** and set path:
```python
POPPLER_PATH = r"C:\path\to\poppler\bin"
```

---

## 🚀 How To Use
1. Place **RC PDF** in folder  
2. Run:
```bash
python RC.py
```
3. Output:
   - `1f.jpg` → Front  
   - `1b.jpg` → Back  
4. Original PDF → moved to `temp`

---

## 🧠 Key Logic
- Reads **multi-page PDF**
- Page 1 → Front  
- Page 2 → Back  
- Crops using:
```python
CROP_W = 2464
CROP_H = 1543
X_START = 0
Y_START = 0
```

- Applies image enhancement:
```python
ALPHA = 1.2   # contrast
BETA  = -40   # brightness
```

---

## ⚡ Features
- ✔️ Auto page detection (front/back)
- ✔️ Image enhancement (contrast + brightness)
- ✔️ Batch processing
- ✔️ Auto file indexing (`1f, 2f...`)
- ✔️ Safe file move (no overwrite)
- ✔️ High-quality output (95%)

---

## ⚠️ Limitations
- Works only for **standard RC PDF format**
- Requires correct page order
- Crop values are fixed

---

## 💡 Tip
If output is misaligned:
- Adjust crop values in code

---

## 🧾 Output Naming
- `1f.jpg` → Front  
- `1b.jpg` → Back  
- Next → `2f, 2b...`

---
