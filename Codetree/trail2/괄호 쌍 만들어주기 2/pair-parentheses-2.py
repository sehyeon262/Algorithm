A = input()
n = len(A)

answer = 0
for i in range(n - 1):
    if A[i] == A[i + 1] == '(':
        for j in range(i + 2, n - 1):
            if A[j] == A[j + 1] == ')':
                answer += 1
            
print(answer)