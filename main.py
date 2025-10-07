import pandas as pd

def read_markdown_file(filename):
    """Читает содержимое Markdown-файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return ''.join(lines)

def convert_to_table(md_text):
    """Простое разделение текста на строки и создание DataFrame"""
    rows = []
    current_row = {}
    for idx, line in enumerate(md_text.strip().splitlines()):
        # Простое правило разделения на строки
        parts = line.strip().split('|')
        
        # Отсекаем пустые строки и ненужные символы
        row = [part.strip() for part in parts if part.strip()]
        
        # Добавляем новую строку в таблицу
        if len(row) > 0:
            rows.append(row)
            
    return pd.DataFrame(rows)

def save_to_excel(df, filename):
    """Экспортирует DataFrame в Excel-файл"""
    df.to_excel(filename, index=False)

if __name__ == '__main__':
    input_file = 'words.md'      # Имя входного Markdown-файла
    output_file = 'done.xlsx'  # Имя выходного Excel-файла

    # Читаем Markdown-файл
    markdown_content = read_markdown_file(input_file)

    # Конвертируем в DataFrame
    table_df = convert_to_table(markdown_content)

    # Экспортируем в Excel
    save_to_excel(table_df, output_file)

    print(f"Данные успешно экспортированы в {output_file}.")