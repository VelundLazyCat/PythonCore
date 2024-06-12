
data = [1, 2, [3, 4, [5, 6]], 7]

# def flatten(data):
#     if len(data) == 0:
#         return []
#     if type(data[0]) == "class 'list'":
#         list1 = flatten(data[0])
#         list2 = flatten(data[1:])
#         return list1+list2
#     else:
#         list1 = data[0]
#         list2 = flatten(data[1:])
#         return list1+list2


def flatten(test_list):
    if isinstance(data, list):
        temp = []
        for ele in data:
            temp.extend(flatten(ele))
        return temp
    else:
        return [data]


print(flatten(data))

a = '''Якщо вхідний список порожній, то:
   Повертаємо порожній список
   Якщо перший елемент списку є списком, то:
  Отримуємо перший список, рекурсивно викликавши функцію з першим елементом списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків
Якщо перший елемент списку не є списком, то:
  Отримуємо перший список із першого елемента списку
  Отримуємо другий список, рекурсивно викликавши функцію з рештою списку без першого елемента
  Повертаємо конкатенацію двох списків'''
