import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]


# 1. 전체 거리 계산
total = 0
for i in range(n - 1):
    total += abs(x[i] - x[i + 1]) + abs(y[i] - y[i + 1])

# 2. 최소 거리 초기화
min_v = sys.maxsize

for i in range(1, n - 1):
    # 3. 기존 거리 계산
    old = abs(x[i - 1] - x[i]) + abs(y[i - 1] - y[i]) + abs(x[i] - x[i + 1]) + abs(y[i] - y[i + 1])

    # 4. 새로운 거리 계산
    new = abs(x[i - 1] - x[i + 1]) + abs(y[i - 1] - y[i + 1])
    
    # 5. 최소 거리 갱신
    min_v = min(min_v, total - old + new)

print(min_v)
    
