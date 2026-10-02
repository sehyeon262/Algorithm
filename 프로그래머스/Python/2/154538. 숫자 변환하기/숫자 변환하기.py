from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])
    
    visited = [0] * (y + 1)
    visited[x] = 1
    
    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt
        
        for nxt in [cur + n, cur * 2, cur * 3]:
            if nxt <= y and not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, cnt + 1)) 

    return -1