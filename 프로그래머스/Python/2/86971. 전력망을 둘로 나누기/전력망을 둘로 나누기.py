# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return
from collections import deque

def solution(n, wires):
    arr = [[] for _ in range(n + 1)]  # 2차원 배열
    
    for a, b in wires:
        arr[a].append(b)
        arr[b].append(a)
    
    def bfs(i, j):
        # 방문 여부 기록
        visited = [False] * (n + 1)
        cnt = 0
        q = deque([i])
        visited[i] = True
        
        while q:
            # cur: 현재 보고 있는 송전탑 번호
            cur = q.popleft()   
            
            # 현재 송전탑 하나 방문했으므로 +1
            cnt += 1
            
            # 현재 송전탑과 연결된 송전탑들 확인
            for nxt in arr[cur]:
                # i번 송전탑과 j번 송전탑을 끊었기 때문 (심지어 양방향이므로)
                if (cur == i and nxt == j) or (cur == j and nxt == i):
                    continue
                    
                # 아직 방문하지 않은 송전탑이라면
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                
        return cnt
            
        
    res = 100
    # 이제 돌아가면서 끊어보자.
    for i in range(1, len(arr)):
        lst = arr[i]   
        
        for j in lst:
            # i: 끊은 전선의 한쪽 송전탑, j: 끊은 전선의 다른쪽 송전탑
            sum1 = bfs(i, j)
                
            if res > abs(sum1 - (n - sum1)):
                res = abs(sum1 - (n - sum1))
                          
    return res
    