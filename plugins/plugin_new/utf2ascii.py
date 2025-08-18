def utf8_to_ascii(input_file_path, output_file_path):
    try:
        # 以 UTF-8 编码打开输入文件
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
            # 将内容转换为 ASCII 编码，忽略非 ASCII 字符
            ascii_content = content.encode('ascii', 'ignore').decode('ascii')
        
        # 以 ASCII 编码打开输出文件并写入转换后的内容
        with open(output_file_path, 'w', encoding='ascii') as output_file:
            output_file.write(ascii_content)
        
        print(f"文件已成功从 UTF-8 转换为 ASCII，保存到 {output_file_path}")
    except FileNotFoundError:
        print(f"错误：未找到输入文件 {input_file_path}")
    except Exception as e:
        print(f"发生错误：{e}")

# 使用示例
if __name__ == "__main__":
    input_file = 'project_new.py'
    output_file = 'project_new.py'
    utf8_to_ascii(input_file, output_file)