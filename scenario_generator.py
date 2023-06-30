def generate_base(file_path):
    with open(file_path, 'r', encoding='utf-8') as text:
        for line in text:
            yield line
