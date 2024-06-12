import os
import sys
import shutil
from pathlib import Path

extensions = {
    'images': ['.JPEG', '.PNG', '.JPG', '.SVG'],
    'video': ['.AVI', '.MP4', '.MOV', '.MKV'],
    'documents': ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'],
    'audio': ['.MP3', '.OGG', '.WAV', '.AMR'],
    'archives': ['.ZIP', '.GZ', '.TAR'],
    'other': '*'
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "gh")
NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
TRANS = {}


for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

matched_folders = []


def rec_walk(folder):
    """ Функція обходу дерева каталогів. Викликає функцію для сортування файлових імен по розділам"""
    matched_files = []
    # список переглянутих папок зберігаємо в глобальній змінній matched_folders
    for name in folder.iterdir():
        if name.is_file():
            matched_files.append(name)
        elif name.is_dir():
            matched_folders.append(name)
            filepath = Path(name)
            matched_files.append(rec_walk(filepath))
    return matched_files


def create_folders(extensions):
    """ Функція створення каталогів для відсортованих файлів"""
    for folder in extensions:
        Path(folder).mkdir(exist_ok=True)


# def normalize(name):
#     """Функція нормалізаціі тексту. Приймає рядок, віддає рядок"""
#     new_name = ''
#     name = name.translate(TRANS)
#     for i in name:
#         # відокремим числа і літери:
#         if (ord(i) > 47 and ord(i) < 58) or (ord(i) < 123 and ord(i) > 96) or (ord(i) > 64 and ord(i) < 91):
#             new_name += i
#         # заміна інших символів на '_'
#         else:
#             new_name += '_'
#     return new_name

# def rename_filename(file_path):
#     """Функція нормалізація обекту Path. Приймає обект, повертає обьект """
#     directory_name = file_path.parent
#     file_name = file_path.name.split('.')
#     file_name[0] = normalize(file_name[0])
#     return directory_name/'.'.join(file_name)


def normalize(file_path):
    """Функція нормалізаціі ім'я файлу. Приймає рядок, віддає рядок """
    directory_name = file_path.parent
    file_name = file_path.name.split('.')
    new_file_name = ''
    for i in file_name[0].translate(TRANS):
        # відокремим числа і літери:
        if (ord(i) > 47 and ord(i) < 58) or (ord(i) < 123 and ord(i) > 96) or (ord(i) > 64 and ord(i) < 91):
            new_file_name += i
        # заміна інших символів на '_'
        else:
            new_file_name += '_'

    return new_file_name + file_path.suffix


def sort_file(file_name, normal_name):
    """Функція сортування файлів по каталогам, приймає старе і нове ім'я, перейменосить файл"""
    global new_name
    for dir_name, suffix in extensions.items():
        if dir_name == 'other':
            new_name = Path(home_path/dir_name/normal_name)
            try:
                os.rename(file_name, new_name)
            except:
                print(f"file <{file_name}> is demaged")
        if file_name.suffix.upper() in suffix:
            new_name = Path(home_path/dir_name/normal_name)
            try:
                os.rename(file_name, new_name)
                break
            except:
                print(f"file <{file_name.name}> is demaged")


def unpack_file(dir_name):
    """ Функція розпаковки архівів у відповідні папки """
    for fl in dir_name.iterdir():
        archive_dir = fl.split('.')
        try:
            shutil.unpack_archive(fl, archive_dir[0])
            print('Разархивовано файл: ', fl)
            os.remove(fl)
        except:
            print(f"{fl}: Не вдалося розпакувати")


def delete_empty_dir(matched_folders):
    """ Фунуція видалення каталогів знайдених при пошуку файлів """
    for dir in matched_folders:
        shutil.rmtree(dir, ignore_errors=True)

# ------------------------------------------------------------------------


if __name__ == '__main__':
    # Змінна для каталогу в якому робится пошук, приймає значення з командного рядка
    home_path = Path(sys.argv[1])

    if not home_path.exists():
        print('This direcyory not exist')
        sys.exit()

    matched_folders = rec_walk(home_path)
    create_folders(extensions)

    for file_name in matched_folders:
        new_name = ''
        normal_name = normalize(file_name.name)
        sort_file(file_name, normal_name)
        print(file_name, ' переміщен в каталог: \n', new_name)
    unpack_file(Path(home_path/'archives'))
    delete_empty_dir(matched_folders)
