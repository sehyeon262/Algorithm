import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
# 주난이 위치, 범인 위치 (행,열)
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

graph = [list(input().strip()) for _ in range(n)]
INF = int(1e8)
dist = [[INF] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((x1, y1))
dist[x1][y1] = 0

while dq:
    x, y = dq.popleft()

    # 도착 지점에 도달하면 조기 종료 (선택 사항이지만 속도 향상에 도움됨)
    if x == x2 and y == y2:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 비용 계산: '1'(친구) 이거나 '#'(범인) 일 때 파동(점프) 1 소모
            if graph[nx][ny] == '1' or graph[nx][ny] == '#':
                cost = dist[x][y] + 1
            else: # '0' (빈칸) 일 때는 즉시 이동 가능
                cost = dist[x][y]

            # 더 적은 비용으로 갈 수 있으면 갱신함
            if dist[nx][ny] > cost:
                dist[nx][ny] = cost

                # 적은 비용 먼저 처리 (0-1 BFS 핵심)
                if graph[nx][ny] == '1' or graph[nx][ny] == '#':
                    dq.append((nx, ny))      # 비용 1 => 덱의 뒤에 넣음
                else:
                    dq.appendleft((nx, ny))  # 비용 0 => 덱의 앞에 넣음

print(dist[x2][y2])