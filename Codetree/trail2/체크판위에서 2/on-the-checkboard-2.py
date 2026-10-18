R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

ans = 0

# 첫 번째로 거쳐 갈 위치 (i, j)
for i in range(1, R - 2):
    # 두 번째로 거쳐 갈 위치 (k, l)
    for j in range(1, C - 2):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                # 조건: 시작점, 첫 번째 경유지, 두 번째 경유지, 도착점의 색이 모두 달라야 함
                if (
                    grid[0][0] != grid[i][j]
                    and grid[i][j] != grid[k][l]
                    and grid[k][l] != grid[R - 1][C - 1]
                ):
                    ans += 1

print(ans)