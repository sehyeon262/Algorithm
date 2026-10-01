from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    # BFS 내부에서는 네트워크를 세지 않는다 → 연결된 컴퓨터들을 방문 처리만 한다.
    def bfs(start):
        q = deque([start])
        visited[start] = 1
        
        while q:
            cur = q.popleft()
            
            for i in range(n):
                # 연결되어 있고 방문을 안 했다면 방문처리 후 q에 넣자 
                if computers[cur][i] and not visited[i]:
                    visited[i] = 1
                    q.append(i)    
            
    
    # 방문하지 않은 컴퓨터를 새로 발견했다는 건 새로운 네트워크 하나를 발견했다는 뜻 -> +1
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)
    
    return answer
