terra=[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power=1

def game(terra, power):
    for i in terra:
        for j in i:            
            if j<=power:
                power=power+j
            else:
               break
    return power
print(game(terra,power))

