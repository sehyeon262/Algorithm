from heapq import heapify, heappop, heappush

def solution(scoville, K):
    # 기존 리스트를 힙으로 변환
    heapify(scoville)
    
    cnt = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        cnt += 1
        first = heappop(scoville)
        second = heappop(scoville)
        mix = first + (second * 2)
        heappush(scoville, mix)  
        
    return cnt
