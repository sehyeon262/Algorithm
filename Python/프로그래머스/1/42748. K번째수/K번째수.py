def solution(array, commands):
    answer = []
    c_num = len(commands)
    
    for a in range(c_num):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])       
    
    return answer