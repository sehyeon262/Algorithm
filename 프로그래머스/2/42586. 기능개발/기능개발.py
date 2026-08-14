from math import ceil

def solution(progresses, speeds):
    answer = []
    lst = []
    length = len(progresses)
    
    # 각 기능이 완료되는 데 걸리는 날짜
    for i in range(length):
        lst.append(ceil((100 - progresses[i]) / speeds[i]))
    
    cnt = 1
    a = 0
    b = 1  
    while b < length:
        if lst[a] >= lst[b]:
            cnt += 1
            b += 1
        else:
            answer.append(cnt)
            a = b
            b += 1
            cnt = 1
            
    # 마지막 묶음도 넣어줌
    answer.append(cnt)    
    return answer
