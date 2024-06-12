import shutil


def create_backup(path, file_name, employee_residence):

    file_path = path+'/'+file_name
    with open(file_path, 'wb') as fh:
        for key, val in employee_residence.items():
            fh.write((f'{key} {val}\n'.encode("utf-8")))
    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name
