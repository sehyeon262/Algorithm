from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_v = 1000000
for lst in combinations(arr, N - 2):
    sum_v = 0
    for i in lst:
        sum_v += i
    min_v = min(min_v, abs(S - sum_v))

print(min_v)