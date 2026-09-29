from math import ceil

def solution(progresses, speeds):
    div = []
    N = len(progresses)
    for n in range(N):
        remain = 100 - progresses[n]
        div.append(ceil(remain / speeds[n]))
    
    answer = []
    # 기준일을 설정해두자!!
    max_day = div[0]
    cnt = 1
    
    for i in range(1, N):
        now_day = div[i]
        
        # 기준일 보다 일찍 끝나면 같은 그룹
        if max_day >= now_day:
            cnt += 1
        else:
            # 기준일 보다 오래 걸리면 이전 그룹 배포 후 기준일 갱신
            answer.append(cnt)
            max_day = now_day
            cnt = 1
    
    # 마지막으로 남은 그룹 배포
    answer.append(cnt)
            
    return answer
        
        
        
    

