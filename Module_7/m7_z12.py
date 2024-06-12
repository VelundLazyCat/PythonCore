

def file_operations(path, additional_info, start_pos, count_chars):

    stroka=''
    with open(path, 'a') as fh:
        fh.write(additional_info +'\n')

    with open(path, 'r') as fh:
        fh.seek(start_pos)
        stroka=fh.read(count_chars)
    return stroka