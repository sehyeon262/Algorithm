def solution(n, lost, reserve):
    res = n
    no = []
    lost.sort()
    reserve.sort()
    
    # 여벌 체육복이 있는 학생도 하나 도난 당했을 경우
    for k in range(len(lost)):
        if lost[k] in reserve:
            reserve.remove(lost[k])
            no.append(lost[k])
    
    for a in (no):
        lost.remove(a)
            
    for i in range(len(lost)):
        if (lost[i] - 1 in reserve):
            reserve.remove(lost[i] - 1)
        elif (lost[i] + 1 in reserve):
            reserve.remove(lost[i] + 1)
        else:
            res -= 1
            
    return res