# 🌡️ Temperature Converter CLI

A simple Python-based **Command Line Interface (CLI)** tool to convert temperatures between **Celsius** and **Fahrenheit**, built using the `argparse` module.

---

## 🚀 Features

- Convert Celsius ↔ Fahrenheit
- Easy to use via command line
- Built using only Python standard libraries

---

## 🛠️ Technologies Used

- Python 3
- `argparse` (built-in module)

---

## 📦 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/VIHARI1106/temperature-converter-cli.git
cd temperature-converter-cli
2. Run the converter
✅ Convert Celsius → Fahrenheit
bash
Copy code
python converter.py 100 --to F
# Output: 100.0°C = 212.00°F
✅ Convert Fahrenheit → Celsius
bash
Copy code
python converter.py 98.6 --to C
# Output: 98.6°F = 37.00°C
📝 Command Line Options
Argument	Description	Required
value	Temperature value to convert	✅
--to [C/F]	Target unit (C for Celsius, F for Fahrenheit)	✅

📷 Sample Output
bash
Copy code
$ python converter.py 32 --to C
32.0°F = 0.00°C

$ python converter.py 37 --to F
37.0°C = 98.60°F
📁 Files in this Repo
converter.py – Main CLI script

README.md – Project description and usage guide

👨‍💻 Author
Prabhugari Vihari
GitHub: @VIHARI1106

yaml
Copy code

---

### ✅ How to Update in GitHub

Once you've pasted this into your `README.md` file:

1. Save it
2. Then run:

```bash
git add README.md
git commit -m "Cleaned up and updated README with usage guide"
git push

