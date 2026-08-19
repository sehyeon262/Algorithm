from heapq import heapify, heappop, heappush

def solution(scoville, K):
    # 기존 리스트 자체를 힙으로 변환
    heapify(scoville)
    
    cnt = 0
    # heapq는 최솟값만 항상 맨 앞에 오도록 유지! 완전히 정렬되는 건 아님 XXXXX
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        cnt += 1
        first = heappop(scoville)
        second = heappop(scoville)
        mix = first + (second * 2)
        heappush(scoville, mix)  
        
    return cnt
