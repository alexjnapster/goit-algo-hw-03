import argparse
import os
import shutil

def parse_arguments():
    parser = argparse.ArgumentParser(description="Копіює файли з вихідної директорії до цільової за типом файлу.")
    parser.add_argument('source', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('destination', type=str, nargs='?', default='dist', help='Шлях до директорії призначення')
    return parser.parse_args()

def copy_files_recursively(source_path, destination_path, dir_cache):
    try:
        for item in os.listdir(source_path):
            full_path = os.path.join(source_path, item)
            if os.path.isdir(full_path):
                copy_files_recursively(full_path, destination_path, dir_cache)
            elif os.path.isfile(full_path):
                handle_file(full_path, destination_path, dir_cache)
    except Exception as e:
        print(f"Не вдалося обробити {source_path}: {e}")

def handle_file(file_path, destination_path, dir_cache):
    try:
        _, file_extension = os.path.splitext(file_path)
        if file_extension:
            extension_dir = file_extension.lstrip('.').lower()
            if extension_dir not in dir_cache:
                directory_path = os.path.join(destination_path, extension_dir)
                if not os.path.exists(directory_path):
                    os.makedirs(directory_path)
                dir_cache.add(extension_dir)
            shutil.copy(file_path, directory_path)
            print(f"Файл {os.path.basename(file_path)} скопійовано до {directory_path}.")
    except Exception as e:
        print(f"Не вдалося скопіювати файл {file_path}: {e}")

def main():
    args = parse_arguments()
    dir_cache = set()
    if not os.path.exists(args.destination):
        os.makedirs(args.destination)
    print(f"Починаємо копіювання з {args.source} до {args.destination}.")
    copy_files_recursively(args.source, args.destination, dir_cache)
    print("Копіювання завершено.")


main()
