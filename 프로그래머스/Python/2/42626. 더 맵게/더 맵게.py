import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) >= 2:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            a = first + (second * 2)
            heapq.heappush(scoville, a)
            cnt += 1
        
        else:
            if scoville[0] < K:
                return -1
    
    return cnt
    