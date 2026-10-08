A = input()
lst = []
for i in A:
    lst.append(i)

n = len(lst)
res = 0
for a in range(n):
    if lst[a] == '(':
        for b in range(a+1, n):
            if lst[b] == ')':
                res += 1

print(res)



    