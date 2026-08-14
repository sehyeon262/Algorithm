def solution(answers):
    res = []
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            score1 += 1
        
        if answers[i] == two[i % len(two)]:
            score2 += 1
        
        if answers[i] == three[i % len(three)]:
            score3 += 1
            
    max_num = max(score1, score2, score3)
    
    if score1 == max_num:
        res.append(1)
    
    if score2 == max_num:
        res.append(2)
    
    if score3 == max_num:
        res.append(3)

    # -------- enumerate 사용 --------
    # for idx, s in enumerate(score):
    #     if s == max(score):
    #         result.append(idx+1)
            
    return res


