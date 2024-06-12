slow1 = 'mi1powerret'
slow2 = 'mi1rewopret'
r = 'power'
w = 5
s = 'p'
rw = True


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    riddle_list = []
    if  reverse:
        for i in riddle:
            riddle_list.append(i)
        riddle_list.reverse()
        riddle = ''
        for j in riddle_list:
            riddle = riddle+j

    count = riddle.find(start_letter)
    if count<0:
        return ''
    else:
        return riddle[count:word_length+count]
    


print(solve_riddle(slow2, w, s,rw))
