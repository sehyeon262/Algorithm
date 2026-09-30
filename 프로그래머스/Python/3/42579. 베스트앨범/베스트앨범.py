# genres[i] = 고유번호가 i인 노래의 장르
# plays[i] = 고유번호가 i인 재생된 횟수

import heapq 
def solution(gen, plays):
    answer = []
    dict = {}
    
    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    for i in range(len(gen)):
        if gen[i] in dict:
            dict[gen[i]] += plays[i]
        else:
            dict[gen[i]] = plays[i]
    
    # 재생된 횟수를 기준으로 내림차순 정렬(dict -> list 형태로 바뀜)
    sort_gen = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    
    
    # 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.

    # dict에서 키를 하나씩 꺼내면서 리스트를 순환시키는 거지.
    for k, _ in sort_gen:
        heap = []
        
        # for문) 만약 gen[i]값이 dict에서 나온 값과 같으면 (-plays[i], i)를 heap에 넣는다
        for i in range(len(gen)):
            if gen[i] == k:
                heapq.heappush(heap, (-plays[i], i))        
        
        # 장르에 속한 곡이 2개 이상이라면
        if len(heap) >= 2:
            # 위 for문 다 돌았으면 play, index = heappop 2번해서 순서대로 answer=[]에 넣는다.
            # 이렇게 했을 때 자동으로 3번 조건은 수용됨. 재생횟수가 같으면 그 뒤에 값중 작은 순으로 뽑기 때문.
            for _ in range(2):
                play, index = heapq.heappop(heap)
                answer.append(index)
        # 장르에 속한 곡이 1개라면
        else:
            play, index = heapq.heappop(heap)
            answer.append(index)
            
                
    return answer
        
        