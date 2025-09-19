
import pandas as pd

def load_csv_with_hash(path):
    return pd.read_csv(path, dtype=str).fillna("")

def compare_csvs(original_path, final_path, output_dir="."):
    # Load both datasets
    original_df = load_csv_with_hash(original_path)
    final_df = load_csv_with_hash(final_path)

    # Index by RowHash for quick lookups
    original_indexed = original_df.set_index("RowHash")
    final_indexed = final_df.set_index("RowHash")

    # 1. Added: in final but not in original
    added_hashes = set(final_indexed.index) - set(original_indexed.index)
    added_rows = final_indexed.loc[list(added_hashes)].reset_index()

    # 2. Removed: in original but not in final
    removed_hashes = set(original_indexed.index) - set(final_indexed.index)
    removed_rows = original_indexed.loc[list(removed_hashes)].reset_index()

    # 3. Modified: shared keys but differing data
    common_hashes = set(original_indexed.index).intersection(set(final_indexed.index))
    modified_rows = []

    for h in common_hashes:
        orig_row = original_indexed.loc[h]
        final_row = final_indexed.loc[h]
        if not orig_row.equals(final_row):
            modified_rows.append(final_row)

    modified_df = pd.DataFrame(modified_rows).reset_index()

    # Output results
    added_rows.to_csv(f"{output_dir}/added.csv", index=False, encoding="utf-8", na_rep="")
    removed_rows.to_csv(f"{output_dir}/removed.csv", index=False, encoding="utf-8", na_rep="")
    modified_df.to_csv(f"{output_dir}/modified.csv", index=False, encoding="utf-8", na_rep="")

    print("✅ Comparison complete.")
    print(f"➕ Added: {len(added_rows)} rows")
    print(f"➖ Removed: {len(removed_rows)} rows")
    print(f"✏️ Modified: {len(modified_df)} rows")

# Example usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compare two hashed CSVs.")
    parser.add_argument("--original", required=True, help="Path to original CSV")
    parser.add_argument("--final", required=True, help="Path to final CSV")
    parser.add_argument("--output-dir", default=".", help="Directory to save added/removed/modified CSVs")
    args = parser.parse_args()

    compare_csvs(args.original, args.final, args.output_dir)
