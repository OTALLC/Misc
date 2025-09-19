
# 📊 CSV Hash Comparator Toolkit

This repository provides a reliable, consistent, and repeatable way to:

1. ✅ Convert Excel files to normalized, hashed CSVs
2. 🔍 Compare two hashed CSVs to find added, removed, or modified rows

Perfect for version tracking, data integrity auditing, or content QA workflows.

---

## 📁 Project Structure

```
csv-hash-comparator/
├── scripts/
│   ├── convert_excel_to_hashed_csv.py   # Converts Excel (.xlsx) to consistent hashed CSV
│   └── compare_hashed_csvs.py           # Compares original vs. final CSVs using RowHash
├── data/
│   ├── example_original.xlsx            # Example original Excel file
│   ├── example_final.xlsx               # Example final Excel file
│   └── diffs/                           # Output directory for added/removed/modified CSVs
└── README.md
```

---

## 🔧 1. Convert Excel to Hashed CSV

### `convert_excel_to_hashed_csv.py`

```bash
python scripts/convert_excel_to_hashed_csv.py
```

This script:
- Loads an Excel sheet (`Detail Report`)
- Skips metadata rows
- Renames columns for consistency
- Generates a `RowHash` (SHA256 of the row’s full contents)
- Saves the result as `Mar_2025_RP_Order_with_Hash_Renamed.csv`

> 📌 You must run this on **both versions** of the Excel file — one becomes the `original`, the other the `final`.

---

## 🔍 2. Compare Hashed CSVs

### `compare_hashed_csvs.py`

```bash
python scripts/compare_hashed_csvs.py \
  --original data/Mar_2025_RP_Order_v1.csv \
  --final data/Mar_2025_RP_Order_v2.csv \
  --output-dir data/diffs/
```

This script:
- Compares two CSVs using the `RowHash` column
- Outputs:
  - `added.csv` – new rows in final
  - `removed.csv` – rows deleted from original
  - `modified.csv` – same row hash, but content changed

---

## 📦 Requirements

```bash
pip install pandas openpyxl
```

---

## 🧪 Testing With Sample Data

Put your `.xlsx` versions in `data/`, run the conversion for both, and then run the comparison.

---

## 🧰 Optional: Hash Function Used

```python
import hashlib

def hash_row(row):
    row_values = ["" if pd.isna(val) else str(val) for val in row]
    row_str = ",".join(row_values)
    return hashlib.sha256(row_str.encode("utf-8")).hexdigest()
```

---

## 🤝 Contributing

1. Fork the repo
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit and push
4. Open a Pull Request!

---

## 📄 License

MIT — use freely, modify responsibly.
