import os
import requests
import time
from urllib.parse import urlparse

def download_files(links_file_path, download_folder):
    # Создаем папку для скачанных файлов, если её нет
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Открываем файл с ссылками
    with open(links_file_path, 'r') as file:
        # Читаем все строки из файла
        links = file.read().splitlines()

        # Перебираем ссылки и скачиваем файлы
        for link in links:
            print(f"Обрабатывается ссылка: {link}")
            try:
                response = requests.get(link, timeout=10)
                if response.status_code == 200:
                    # Извлекаем имя файла из ссылки
                    parsed_url = urlparse(link)
                    file_name = os.path.join(download_folder, os.path.basename(parsed_url.path))
                    
                    # Сохраняем файл в папку для скачанных файлов
                    with open(file_name, 'wb') as file:
                        file.write(response.content)
                    
                    print(f"Файл {file_name} успешно скачан.")
                else:
                    print(f"Не удалось скачать файл по ссылке: {link}")
            except Exception as e:
                print(f"Ошибка при скачивании файла по ссылке {link}: {str(e)}")

            # Добавляем паузу между запросами
            time.sleep(1)

if __name__ == "__main__":
    # Путь к файлу с ссылками
    links_file_path = r'C:\python\linck.txt'
    
    # Папка для скачанных файлов
    download_folder = r'C:\python\Скачанные файлы'
    
    # Вызываем функцию для скачивания файлов
    download_files(links_file_path, download_folder)
