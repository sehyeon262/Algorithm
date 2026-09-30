def solution(citations):
    N = len(citations)
    citations.sort()
        
    for i in range(N):
        if citations[i] >= N - i:
            return N - i
            
    return 0
    
    
# ---------------예시-----------------------
# 정렬된 citations = [1, 10, 10]
# 전체 논문의 수 N = 3

# i = 0 → 남은 논문 [1, 10, 10], 총 3편
#         가장 적은 인용 횟수가 1 → 모두 3번 이상 인용된 것은 아님

# i = 1 → 남은 논문 [10, 10], 총 2편
#         가장 적은 인용 횟수가 10 → 모두 2번 이상 인용됨
#         따라서 2 반환
