from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
      
    # Counter(리스트) => 각 원소의 등장 횟수를 자동으로 세어주는 dict 비슷한 자료구조 !!!!!!!
    for j in range(len(discount) - 9):
        if dic == Counter(discount[j:j+10]):
            answer += 1
        
    return answer
