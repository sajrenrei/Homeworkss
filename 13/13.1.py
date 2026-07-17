import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cleaned_content = re.sub(r'<[^>]*>', '', html_content)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print(f"Файл успішно очищено! Результат збережено у: {result_file}")


# --- БЛОК ДЛЯ ПЕРЕВІРКИ РОБОТИ КОДУ ---
if __name__ == "__main__":
    test_html_content = """
    <html>
        <head><title>Тестова сторінка</title></head>
        <body>
            <h1>Привіт, світе!</h1>
            <p>Це <b>простий</b> текст для перевірки нашої функції.</p>
            <div class="footer">Кінець файлу.</div>
        </body>
    </html>
    """

    with open('draft.html', 'w', encoding='utf-8') as f:
        f.write(test_html_content)

    delete_html_tags('draft.html', 'cleaned.txt')

    print("\nВміст очищеного файлу (cleaned.txt):")
    print("-" * 40)
    with open('cleaned.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    print("-" * 40)