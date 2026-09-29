# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return

from collections import deque

def solution(maps):
    answer = -1
    
    # 동 서 남 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    rows = len(maps)
    cols = len(maps[0])
    
    # 방문 여부 및 이동 거리 기록할 배열
    visited = [[False] * cols for _ in range(rows)]
    
    # 큐 생성 및 (시작점, 현재까지 이동한 거리) 삽입
    q = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while q:
        # 현재 위치 꺼내기
        x, y, dist = q.popleft()
        
        # 상대 팀 진영에 도착하면 return
        if x == rows-1 and y == cols - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 배열 범위 안에 있다면
            if 0 <= nx < rows and 0 <= ny < cols:
                # 방문하지 않았고, 벽이 아니라면
                if visited[nx][ny] == False and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))                    
    
    return answer