import os
import time

directory ="/Users/elinalitovskaa/Documents/Urban/Python/07_Работа с файлами/01_работа с файлами"

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        filetime = os.path.getmtime(file_path)
        file_dir = os.path.dirname(file_path)
        file_size = os.path.getsize(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    print(
        f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, '
        f'Время изменения: {formatted_time}, Родительская директория: {file_dir}')



