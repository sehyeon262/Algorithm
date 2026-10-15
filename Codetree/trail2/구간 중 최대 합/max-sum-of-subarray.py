n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_v = -100000
for i in range(n - k + 1):
    sum_v = 0
    for j in range(k):
        sum_v += arr[i + j]
    max_v = max(max_v, sum_v)

print(max_v)