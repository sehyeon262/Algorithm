from collections import deque

def solution(priorities, location):
    order = 0 
    
    # (원래 위치, 우선순위)
    q = deque(list(enumerate(priorities)))
    
    while q:
        # 큐의 맨 앞 프로세스 하나 꺼냄
        now = q.popleft()
        
        higher_exists = False
        
        # 현재 큐 안에 방금 꺼낸 프로세스보다 우선순위 높은 거 하나라도 있는 지 확인
        for p in q:
            if p[1] > now[1]:
                higher_exists = True
                break
        
        # 있으면 뒤로 넣음
        if higher_exists:
            q.append(now)
        # 없으면 실행
        else:
            order += 1
            
            # 찾는 프로세스가 맞다면 return
            if now[0] == location:
                return order