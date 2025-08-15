#!/usr/bin/env python3
import csv
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python3 csv_to_sql.py <csv_file> <table_name>")
    sys.exit(1)

csv_path = sys.argv[1]
table_name = sys.argv[2]

if not os.path.isfile(csv_path):
    print(f"File not found: {csv_path}")
    sys.exit(1)

output_path = os.path.splitext(csv_path)[0] + "_insert_statements.sql"

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # First row = column names

    with open(output_path, "w", encoding="utf-8") as f:
        for row in reader:
            values = []
            for value in row:
                value = value.strip()
                if value == "":
                    values.append("NULL")
                elif value.replace('.', '', 1).isdigit():
                    values.append(value)
                else:
                    values.append("'" + value.replace("'", "''") + "'")
            insert_sql = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(values)});"
            f.write(insert_sql + "\n")

print(f"✅ SQL insert statements saved to: {output_path}")

