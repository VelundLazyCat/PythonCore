
path = 'recipe.txt'
search_id = '60b90c1c13067a15887e1ae1'


def get_recipe(path, search_id):

    recipe_dict = {"id": '', "name": '', "ingredients": ''}
    flag = False

    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            if line.find(search_id) >= 0:
                line = line.removesuffix('\n')
                recipe_line = line.split(",")
                # recipe_line[len(recipe_line)-1]
                recipe_dict.update(
                    [("id", recipe_line[0]), ("name", recipe_line[1]), ("ingredients", recipe_line[2:])])
                flag = True
                break

    if flag:
        return recipe_dict
    else:
        return None


print(get_recipe(path, search_id))
