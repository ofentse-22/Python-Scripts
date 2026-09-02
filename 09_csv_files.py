"""Practical 09: CSV files.

Topics from the notes:
- Importing csv
- Writing rows
- Reading rows
- Using a delimiter
"""

import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
GENERATED_DIR = BASE_DIR / "generated_files"
CSV_PATH = GENERATED_DIR / "shopping_list.csv"


def write_csv_file():
    GENERATED_DIR.mkdir(exist_ok=True)

    rows = [
        ["Item", "Cost"],
        ["Coffee", "2.00"],
        ["Cake", "5.00"],
        ["Milk", "1.75"],
    ]

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

    print("CSV file created:", CSV_PATH)


def read_csv_file():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as csv_file:
        data_from_file = csv.reader(csv_file, delimiter=",")
        rows = list(data_from_file)

    print("Rows from CSV:")
    for row in rows:
        print(row)

    return rows


def calculate_total(rows):
    total = 0

    for item, cost in rows[1:]:
        total += float(cost)
        print("{0:<10} R{1:>6.2f}".format(item, float(cost)))

    print("-" * 18)
    print("{0:<10} R{1:>6.2f}".format("Total", total))


def main():
    write_csv_file()
    print()
    rows = read_csv_file()
    print()
    calculate_total(rows)


if __name__ == "__main__":
    main()
