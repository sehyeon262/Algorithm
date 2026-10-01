def solution(n, computers):
    answer = 0  # 네트워크 개수
    visited = [0] * n
    
    # 방문 처리만 하는 함수라 return 없어도 됨!!
    def dfs(i):
        visited[i] = 1
        
        for k in range(n):
            # i와 k가 연결되어 있고, k를 아직 방문하지 않았다면
            if computers[i][k] == 1 and not visited[k]:
                dfs(k)
                
                
    for i in range(n):
        if not visited[i]:
            # 새로운 네트워크 발견
            answer += 1
            dfs(i)
                  
    return answer
                