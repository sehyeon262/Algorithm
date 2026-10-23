T = int(input())

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, nums):
    if len(nums) == 7:
        answer.add(nums)
        return
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        # 범위 안 이면
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, nums + str(arr[nx][ny]))

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    answer = set() 
    for i in range(4):
        for j in range(4):
            nums = str(arr[i][j])
            dfs(i, j, nums)

    print(f'#{tc} {len(answer)}')