def solution(a, b):
    answer = 0
    if a > b:
        temp = a
        a = b
        b = temp
        
    while a <= b:
        answer += a
        a += 1
        
    return answer