data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


# def decode(data):
#     temp=[]
#     count=0
#     while len(data)>0:
#         count=data[0]
#         if isinstance(count,str):
#             a=data.pop(0)
#             temp.append(a)
#         else:
#             count = data.pop(0)
#             for i in range(count-1):
#                 temp.append(a)

#     return temp


def decode(data):

    if not data:
        return []
    else:
        char = data[0]
        quont = data[1]
        char = [char for i in range(quont)]
        return char + decode(data[2:])


print(decode(data))
