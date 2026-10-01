from collections import deque 

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    # start 위치에서 target 문자까지의 최단거리 탐색    
    def bfs(i, j, target):
        # 'S'->'L' 찾을때랑 'L'->'E' 찾을 때 각각 방문여부를 만들어야 함.
        visited = [[0] * col for _ in range(row)]
        
        # (x좌표, y좌표, 현재까지 걸린 시간)
        q = deque([(i, j, 0)])
        visited[i][j] = 1
        
        # 상, 하, 좌, 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y, time = q.popleft()
            
            # 목표 지점에 도착했다면 좌표와 시간 반환함.
            if maps[x][y] == target:
                return (x, y, time)
                            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                # 범위 안이고 벽이 아니라면
                if 0 <= nx < row and 0 <= ny < col and not maps[nx][ny] == 'X':
                    
                    # 아직 방문하지 않았다면
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny, time + 1))
        
        # 목표 지점까지 갈 수 없는 경우
        return None 
    
    # 시작지점 'S' 찾기
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                
                # 1. S -> L 최단거리
                result1 = bfs(i, j, 'L')
                # 레버까지 갈 수 없다면 탈출 불가능
                if result1 is None:
                    return -1
                a, b, time1 = result1
                
                # 2. L -> E 최단거리
                result2 = bfs(a, b, 'E')
                # 출구까지 갈 수 없다면 탈출 불가능
                if result2 is None:
                    return -1
                _, _, time2 = bfs(a, b, 'E')
    
    # S -> L 시간 + L -> E 시간
    return time1 + time2 


# S 위치 찾기
# → BFS로 L까지 최단거리
# → L에서 다시 BFS로 E까지 최단거리
# → 둘 중 하나라도 못 가면 -1
# → 둘 다 갈 수 있으면 두 거리의 합 반환