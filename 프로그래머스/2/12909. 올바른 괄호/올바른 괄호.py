def solution(s):
    
    cnt = 0
    
    for char in s:
        if char == "(":
            cnt += 1
        else:
            cnt -= 1
        
        # 닫는 괄호가 먼저 나오면 틀린거임
        if cnt < 0:
            return False   
    if cnt == 0:
        return True
    else:
        return False