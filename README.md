# 📬 Mail Merge Project

This is a simple yet practical **Python automation project** that generates personalized invitation letters for multiple people automatically.  
It reads a list of names from a text file, inserts each name into a predefined letter template, and saves each customized letter as a `.docx` file.

---

## ✨ Features

- Reads guest names from a text file (`invited_names.txt`)
- Replaces placeholders (e.g., `[name]`) in a letter template
- Creates personalized invitation letters automatically
- Saves each letter as a Word document (`.docx`) in the output folder
- Uses the `python-docx` library for Word file generation

---


---

## ⚙️ Requirements

Make sure you have **Python 3.8+** installed.

Install dependencies using pip:

```bash
pip install python-docx
