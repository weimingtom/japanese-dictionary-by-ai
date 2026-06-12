import csv
import json

# 读取CSV文件
data = []
try:
    with open('jpwords_4_1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) >= 3:
                # 按照要求分配列：第1列->reading, 第2列->japanese, 第3列->meaning
                reading = row[0].strip()
                japanese = row[1].strip()
                meaning = row[2].strip()
                
                # 创建JavaScript对象
                js_obj = {
                    "reading": reading,
                    "japanese": japanese,
                    "meaning": meaning
                }
                data.append(js_obj)
                
                # 仅输出前几个条目进行验证
                if i < 5:
                    print(f"Entry {i}: reading='{reading}', japanese='{japanese}', meaning='{meaning}'")
            elif len(row) > 0:  # 处理少于3列的行
                print(f"Warning: Row {i} has fewer than 3 columns: {row}")
                
    print(f"Successfully read {len(data)} entries from CSV file")
    
    # 生成JavaScript代码
    js_code_lines = ["// Generated from jpwords_4_1.csv", "const dictionaryData = ["]
    
    for i, entry in enumerate(data):
        # 转义特殊字符以确保JavaScript语法正确
        reading = entry["reading"].replace('"', '\\"').replace("'", "\\'").replace("\n", "\\n").replace("\r", "\\r")
        japanese = entry["japanese"].replace('"', '\\"').replace("'", "\\'").replace("\n", "\\n").replace("\r", "\\r")
        meaning = entry["meaning"].replace('"', '\\"').replace("'", "\\'").replace("\n", "\\n").replace("\r", "\\r")
        
        js_code_lines.append(f'    {{ reading: "{reading}", japanese: "{japanese}", meaning: "{meaning}" }},')
    
    js_code_lines.append("];")
    
    # 保存到文件
    js_code = "\n".join(js_code_lines)
    with open('generated_dictionary.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    print(f"Generated JavaScript code with {len(data)} entries and saved to 'generated_dictionary.js'")
    
    # 显示生成的部分代码
    print("\nFirst few lines of generated JavaScript:")
    for i in range(min(10, len(js_code_lines))):
        print(js_code_lines[i])
    
except UnicodeDecodeError as e:
    print(f"Failed to read with UTF-8 encoding: {e}")
    print("Try converting the file to proper UTF-8 encoding first.")
except Exception as e:
    print(f"Error reading file: {e}")