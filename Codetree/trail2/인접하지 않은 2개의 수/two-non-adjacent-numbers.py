n = int(input())
numbers = list(map(int, input().split()))

max_n = -1000
for i in range(n - 2):
    for j in range(i + 2, n):
        num = numbers[i] + numbers[j]
        if max_n < num:
            max_n = num

print(max_n)
