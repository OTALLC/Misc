
import pandas as pd
import hashlib

def hash_row(row):
    row_values = ["" if pd.isna(val) else str(val) for val in row]
    row_str = ",".join(row_values)
    return hashlib.sha256(row_str.encode("utf-8")).hexdigest()

def convert_excel_to_hashed_csv(
    excel_path,
    output_csv_path,
    sheet_name="Detail Report",
    skiprows=7
):
    df = pd.read_excel(excel_path, sheet_name=sheet_name, skiprows=skiprows)

    column_renames = {
        df.columns[0]: "Date",
        df.columns[1]: "Roleplayer Time",
        df.columns[2]: "Session Time",
        df.columns[3]: "Class",
        df.columns[4]: "Lab / PE Title",
        df.columns[5]: "Session Location",
        df.columns[6]: "Reporting Location",
        df.columns[7]: "Roleplayers Total",
        df.columns[8]: "Roleplayer Duration",
        df.columns[9]: "Division",
        df.columns[10]: "Male",
        df.columns[11]: "Female",
        df.columns[12]: "Any Sex",
    }

    df = df.rename(columns=column_renames)
    df.insert(0, "RowHash", df.apply(hash_row, axis=1))
    df.to_csv(output_csv_path, index=False, encoding="utf-8", na_rep="")

    print(f"✅ Hashed CSV saved to: {output_csv_path}")

if __name__ == "__main__":
    convert_excel_to_hashed_csv(
        excel_path="Order.xlsx",
        output_csv_path="Mar_2025_RP_Order_with_Hash_Renamed.csv"
    )
