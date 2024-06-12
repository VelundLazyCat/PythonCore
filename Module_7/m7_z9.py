my_list = [4, 6, 1, 3]

def all_sub_lists(data):
    new_data = [[]]
    
    
    for i in range(len(data)):
        for j in range(len(data)):
            if j+i+1<=len(data):
               t=j+i+1
               new_data.append(data[j:t])
            else:
                break
        
    return new_data


print(all_sub_lists(my_list))