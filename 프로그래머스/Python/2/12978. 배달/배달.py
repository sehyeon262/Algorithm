import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    def dijkstra():
        # 다익스트라 필수 1: 최단 거리 기록장 (dist 배열)
        dist = [float('inf')] * (N + 1)
        dist[1] = 0
        
        # 다익스트라 필수 2: 우선순위 큐 (탐색 바구니)
        q = [(0, 1)]   # (비용, 마을 번호)
        
        while q:
            cur_cost, cur_n = heapq.heappop(q)
            
            # dist에 이미 더 적은 비용이 있다면 이 경로는 더이상 탐색 가치 없으므로 무시! 
            if dist[cur_n] < cur_cost:
                continue
            
            # 현재 마을과 연결된 다른 길들 하나씩 확인함 
            for next_cost, next_n in graph[cur_n]:
                # 다음 마을로 가는 새로운 총 비용 계산함
                new_cost = cur_cost + next_cost
                # 새로운 총 비용이 기존 dist에 적힌 비용보다 더 적다면 
                if dist[next_n] > new_cost:
                    # 1) 적은 비용으로 갱신하고
                    dist[next_n] = new_cost
                    # 2) 이 새로운 경로를 통해 다른 마을로 가는 더 빠른 길이 있을 수 있으므로 q에 추가!
                    heapq.heappush(q, (new_cost, next_n))
                    
        return dist

    for lst in road:
        # 양방향 (비용, 마을 번호)
        graph[lst[0]].append((lst[2], lst[1]))
        graph[lst[1]].append((lst[2], lst[0]))
    
    distances = dijkstra()
    answer = 0
    for i in distances:
        if i <= K:
            answer += 1
    return answer
    