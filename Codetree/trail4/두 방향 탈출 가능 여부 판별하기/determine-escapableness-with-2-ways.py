n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    
    visited[x][y] = 1

    # 아래, 오른쪽
    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                if dfs(nx, ny) == 1:
                    return 1
    
    return 0

print(dfs(0, 0))
