def solution(sizes):
    res = 1
    for i in range(len(sizes)):
        sizes[i].sort()
    
    for k in range(2):
        max_num = sizes[0][k]
        for j in range(1, len(sizes)):
            if sizes[j][k] > max_num:
                max_num = sizes[j][k]
                
        res *= max_num
    return res