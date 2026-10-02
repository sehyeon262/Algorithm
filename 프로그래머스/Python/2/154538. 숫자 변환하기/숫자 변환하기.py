# 목표 : x를 y로 변환하기 위해 필요한 최소 연산 횟수
# 조건
#   1. x에 n을 더합니다
#   2. x에 2를 곱합니다.
#   3. x에 3을 곱합니다.
# 알고리즘 후보 : bfs (최소 연산 횟수, 비용이 1회로 동일)

from collections import deque

def solution(x, y, n):
    cnt = 0
    
    # (현재 값, 횟수)
    def bfs(x, cnt):
        # visited = 이 숫자는 이미 더 빠르거나 같은 횟수로 도달해봤으니 다시 볼 필요 없다.
        visited = [0] * (y + 1)
        # 시작값 방문 처리
        visited[x] = 1
        q = deque([(x, 0)])
        
        while q:
            cur, cnt = q.popleft()
            
            # 결과값에 도달했으면 return
            if cur == y:
                return cnt
            
            for nxt in [cur + n, cur * 2, cur * 3]:
                if nxt <= y and not visited[nxt]:
                    visited[nxt] = 1
                    q.append((nxt, cnt + 1))
        
        # 끝까지 못 찾았으면         
        return -1
        
    return bfs(x, n)
    