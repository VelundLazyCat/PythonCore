
path = 'cats_base.txt'
# cats_base=['60b90c1c13067a15887e1ae1,Tayson,3','60b90c2413067a15887e1ae2,Vika,1','60b90c2e13067a15887e1ae3,Barsik,2','60b90c3b13067a15887e1ae4,Simon,12','60b90c4613067a15887e1ae5,Tessi,5']
# fh = open(path, 'w')
# for i in cats_base:
#     fh.write(i+'\n')
# fh.close()


def get_cats_info(path):
    cat_list = []
    cats_id = ["id", "name", "age"]

    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            cat_line = line.split(",")
            cat_line[2] = cat_line[2].removesuffix('\n')
            cat_list.append(dict(zip(cats_id, cat_line)))

    return cat_list


print(get_cats_info(path))
