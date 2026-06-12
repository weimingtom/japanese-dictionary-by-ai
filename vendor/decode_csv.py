import csv

def try_decode_with_multiple_encodings(file_path):
    encodings = ['utf-8', 'shift-jis', 'gbk', 'big5', 'utf-8-sig', 'euc-jp', 'iso-2022-jp']
    
    for encoding in encodings:
        try:
            print(f"Trying encoding: {encoding}")
            with open(file_path, 'r', encoding=encoding) as f:
                reader = csv.reader(f)
                rows = list(reader)
                
                # 检查前几行是否包含有意义的日语字符
                sample_text = ''.join([''.join(row) for row in rows[:10]])
                
                # 如果能识别出一些常见的日文字符，则认为解码成功
                has_japanese_chars = any('\u3040' <= char <= '\u309F' or  # 平假名
                                        '\u30A0' <= char <= '\u30FF' or  # 片假名
                                        '\u4E00' <= char <= '\u9FFF'     # 汉字
                                        for char in sample_text)
                
                if has_japanese_chars or len(sample_text) > 0:
                    print(f"Successfully read with {encoding} encoding")
                    print("First 5 rows:")
                    for i, row in enumerate(rows[:10]):  # 显示更多行来看清结构
                        print(f"Row {i}: {row}")
                    return rows, encoding
                    
        except UnicodeDecodeError:
            print(f"Failed with {encoding} encoding")
            continue
        except Exception as e:
            print(f"Error with {encoding} encoding: {e}")
            continue
    
    print("Could not decode file with any encoding")
    return None, None

rows, encoding = try_decode_with_multiple_encodings('jpwords_4_1.csv')

if rows:
    print(f"\nFound {len(rows)} total rows in the CSV file")
    print("CSV appears to have 3 columns based on the structure:")
    print("- Column 1: Reading (furigana/pronunciation)")
    print("- Column 2: Japanese word/kanji")
    print("- Column 3: Meaning/translation")
    
    # 根据要求，创建JavaScript格式的数据
    print("\nConverting to JavaScript dictionaryData format...")
    js_data = []
    
    # 跳过标题行
    for i, row in enumerate(rows[1:101]):  # 取前100个示例看看
        if len(row) >= 3:
            reading = row[0].strip()
            japanese = row[1].strip()
            meaning = row[2].strip()
            
            if reading or japanese or meaning:  # 确保至少有一个字段非空
                js_entry = f"    {{ japanese: \"{japanese}\", reading: \"{reading}\", meaning: \"{meaning}\" }},"
                js_data.append(js_entry)
    
    print("Sample JavaScript data:")
    for entry in js_data[:10]:  # 显示前10个
        print(entry)
else:
    print("Could not decode the CSV file")