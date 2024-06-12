data = [[3,1,2],[3,4], [5,6]]

def data_preparation(list_data):
    new_data=[]
    for i in list_data:
        if len(i)>2:
            i=i.copy()
            i.sort()
            i.pop(0)
            i.pop(-1)
            new_data.extend(i)
        else:
            new_data.extend(i)
    new_data.sort(reverse=True)
    return new_data

print(data_preparation(data))