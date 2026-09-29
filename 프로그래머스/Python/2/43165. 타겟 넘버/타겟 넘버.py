def solution(numbers, target):
    answer = 0
    
    def dfs(index, now_sum):
        nonlocal answer
        
        # 종료 조건 (모든 숫자를 다 사용했을 때)
        if index == len(numbers):
            if now_sum == target:
                answer += 1
            return
        
        # 재귀 호출(더하는 길, 빼는 길)
        dfs(index + 1, now_sum + numbers[index])
        dfs(index + 1, now_sum - numbers[index])
        
    dfs(0, 0)
    return answer