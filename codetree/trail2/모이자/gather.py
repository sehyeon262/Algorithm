import sys
n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_v = sys.maxsize
for i in range(n):
    sum_v = 0
    for j in range(n):
        sum_v += A[j] * abs(i - j)
    
    if min_v > sum_v:
        min_v = sum_v
print(min_v)