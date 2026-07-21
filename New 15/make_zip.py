import zipfile

# Перелік файлів, які треба упакувати
files_to_zip = ['human.py', 'student.py', 'exceptions.py', 'group.py', 'main.py']

# Назва майбутнього архіву
with zipfile.ZipFile('homework_solution.zip', 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)

print("Архів успішно створено!")