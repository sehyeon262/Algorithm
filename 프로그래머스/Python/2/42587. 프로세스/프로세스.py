from collections import deque

def solution(priorities, location):
    
    # (인덱스, 우선순위) 형태로 큐에 넣음!
    q = deque(enumerate(priorities))

    max_n = max(priorities)
    cnt = 1
    
    while q:
        index, num = q.popleft()
        
        if max_n == num:
            if index == location:
                return cnt
                break
            cnt += 1
            _, max_n = max(q, key=lambda x:x[1])
            continue
        else:
            q.append((index, num))
        
            
            
        
            
        