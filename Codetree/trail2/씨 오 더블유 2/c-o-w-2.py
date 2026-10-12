n = int(input())
S = list(input())

answer = 0
for i in range(n):
    if S[i] == 'C':
        for j in range(i, n):
            if S[j] == 'O':
                for k in range(j, n):
                    if S[k] == 'W':
                        answer += 1

print(answer)