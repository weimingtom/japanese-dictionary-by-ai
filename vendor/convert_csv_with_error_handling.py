import csv
import re

def clean_text(text):
    """清理文本，移除或替换无法处理的字符"""
    if not isinstance(text, str):
        return str(text) if text is not None else ""
    
    # 移除控制字符，保留日文字符
    cleaned = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    return cleaned

# 读取CSV文件 - 使用错误处理
data = []
try:
    with open('jpwords_4_1.csv', 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if len(row) >= 3:
                # 按照要求分配列：第1列->reading, 第2列->japanese, 第3列->meaning
                reading = clean_text(row[0].strip())
                japanese = clean_text(row[1].strip())
                meaning = clean_text(row[2].strip())
                
                # 确保只处理有意义的数据
                if reading or japanese or meaning:
                    # 创建JavaScript对象
                    js_obj = {
                        "reading": reading,
                        "japanese": japanese,
                        "meaning": meaning
                    }
                    data.append(js_obj)
                    
                    # 仅输出前几个条目进行验证
                    if i < 10:
                        print(f"Entry {i}: reading='{reading}', japanese='{japanese}', meaning='{meaning}'")
            elif len(row) > 0:  # 处理少于3列的行
                print(f"Warning: Row {i} has fewer than 3 columns: {row}")
                
    print(f"Successfully read {len(data)} entries from CSV file")
    
    # 生成JavaScript代码
    js_code_lines = ["// Generated from jpwords_4_1.csv", "// 日语词典数据", "const dictionaryData = ["]
    
    for i, entry in enumerate(data):
        # 转义特殊字符以确保JavaScript语法正确
        reading = entry["reading"].replace('"', '\\"').replace("'", "\\'").replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r")
        japanese = entry["japanese"].replace('"', '\\"').replace("'", "\\'").replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r")
        meaning = entry["meaning"].replace('"', '\\"').replace("'", "\\'").replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r")
        
        js_code_lines.append(f'    {{ reading: "{reading}", japanese: "{japanese}", meaning: "{meaning}" }},')
    
    js_code_lines.append("];")
    
    # 保存到文件
    js_code = "\n".join(js_code_lines)
    with open('generated_dictionary.js', 'w', encoding='utf-8', errors='replace') as f:
        f.write(js_code)
    
    print(f"Generated JavaScript code with {len(data)} entries and saved to 'generated_dictionary.js'")
    
    # 显示生成的部分代码
    print("\nFirst few lines of generated JavaScript:")
    for i in range(min(15, len(js_code_lines))):
        print(js_code_lines[i])
    
except Exception as e:
    print(f"Error reading file: {e}")
    import traceback
    traceback.print_exc()