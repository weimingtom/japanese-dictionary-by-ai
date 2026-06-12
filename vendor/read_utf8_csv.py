import csv

try:
    with open('jpwords_4_1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("Successfully opened file with UTF-8 encoding")
        print("First 10 rows:")
        for i, row in enumerate(reader):
            if i < 10:
                print(f"Row {i}: {row}")
            else:
                break
        print(f"Total rows read: {i+1}")
except UnicodeDecodeError as e:
    print(f"Failed to read with UTF-8 encoding: {e}")
except Exception as e:
    print(f"Error reading file: {e}")