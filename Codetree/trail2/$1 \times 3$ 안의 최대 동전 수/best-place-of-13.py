n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_n = 0
for i in range(n):
    for j in range(n - 2):
        max_n = max(max_n, grid[i][j] + grid[i][j + 1] + grid[i][j + 2])

print(max_n)