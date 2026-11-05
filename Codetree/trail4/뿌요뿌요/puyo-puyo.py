n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y, num):
    global cnt
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == num and not visited[nx][ny]:
                cnt += 1
                dfs(nx, ny, num)

    return cnt

boom = 0
max_n = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if not visited[i][j]:
            res = dfs(i, j, grid[i][j])
            # 터지는 블럭수가 있다면
            if res + 1 >= 4:    
                boom += 1
            max_n = max(max_n, res + 1)

print(boom, max_n)