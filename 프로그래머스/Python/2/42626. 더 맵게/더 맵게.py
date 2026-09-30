# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
from heapq import heapify, heappush, heappop

def solution(scoville, K):
    # 리스트를 힙으로 변환
    heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        # 원소가 2개 이상일때
        if len(scoville) >= 2:
            first = heappop(scoville)
            second = heappop(scoville)
            sco = first + (second * 2)
            heappush(scoville, sco)
            cnt += 1
        # 원소가 1개일 때
        else:
            if scoville[0] < K:
                return -1
    
    return cnt
    