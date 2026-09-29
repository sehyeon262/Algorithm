# deque, enumerate 안 쓴 풀이

def solution(priorities, location):
    order = 0   # 실행 순서
    
    while priorities:
        # 맨 앞보다 더 높은 순위 있으면 뒤로 보냄
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        
        # 맨 앞이 가장 높은 순위면 실행
        else:
            priorities.pop(0)
            order += 1
            
            # 찾던 프로세스 라면 return
            if location == 0:
                return order
            
            location -= 1
