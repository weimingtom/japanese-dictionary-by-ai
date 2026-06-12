import csv

# 尝试不同的编码格式读取CSV文件
encodings = ['utf-8', 'shift-jis', 'gbk', 'big5', 'utf-8-sig']

for encoding in encodings:
    try:
        print(f"Trying encoding: {encoding}")
        with open('jpwords_4_1.csv', 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            rows = list(reader)
            print(f"Successfully read with {encoding} encoding")
            print("First 5 rows:")
            for i, row in enumerate(rows[:5]):
                print(f"Row {i}: {row}")
            break
    except UnicodeDecodeError:
        print(f"Failed with {encoding} encoding")
        continue
    except Exception as e:
        print(f"Error with {encoding} encoding: {e}")
        continue