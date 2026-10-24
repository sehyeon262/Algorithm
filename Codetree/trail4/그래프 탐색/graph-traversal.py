n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited = [0] * (n + 1)
visited[1] = 1
graph = [[0] * (n + 1) for _ in range(n + 1)]

for a, b in edges:
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node):
    global cnt
    for i in range(1, n + 1):
        if not visited[i] and graph[node][i]:
            cnt += 1
            visited[i] = 1
            dfs(i)
    return cnt

cnt = 0
print(dfs(1))
