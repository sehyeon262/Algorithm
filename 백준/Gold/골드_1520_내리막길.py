#  제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

M, N = map(int, input().split())
arr = []

for _ in range(M):
    row = list(map(int, input().split()))
    arr.append(row)

# 하, 우
dx = [1, 0]
dy = [0, 1]

cost = arr[0][0]

for i in range()