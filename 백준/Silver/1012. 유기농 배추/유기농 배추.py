# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다
# 0 : 없음, 1: 배추 

from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                q = deque([(i, j)])
                arr[i][j] = 0   # 방문 처리 (없애기)

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        
                        if 0 <= nx < N and 0 <= ny < M:
                            if arr[nx][ny] == 1:
                                q.append((nx, ny))
                                arr[nx][ny] = 0

    print(cnt)                   
