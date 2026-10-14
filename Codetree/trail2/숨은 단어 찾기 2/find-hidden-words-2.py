N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

answer = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == 'L':
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                nx2 = nx + dx[i]
                ny2 = ny + dy[i]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'E':
                    if 0 <= nx2 < N and 0 <= ny2 < M and arr[nx2][ny2] == 'E':
                        answer += 1

print(answer)