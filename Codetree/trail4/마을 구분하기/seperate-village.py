n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def dfs(x, y):
    global cnt

    visited[x][y] = 1
    cnt += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


res = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for a in res:
    print(a)