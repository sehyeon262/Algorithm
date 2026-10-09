from itertools import combinations
N = int(input())
A = list(map(int, input().split()))

answer = 0
for lst in combinations(A, 3):
    a, b, c = lst
    if a <= b <= c:
        answer += 1

print(answer)