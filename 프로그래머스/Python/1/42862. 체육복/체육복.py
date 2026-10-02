def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    cnt = 0
    
    # 여벌인 학생이 도난 당했을 경우 -> 미리 삭제
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # sorted() => 정렬된 새로운 리스트를 반환!!!
    lost =  sorted(lost_set - reserve_set)
    reserve = sorted(reserve_set - lost_set)
    
       
    for i in range(len(lost)):
        before = lost[i] - 1
        after = lost[i] + 1
    
        if  before in reserve:
            cnt += 1
            reserve.remove(before)
            
        elif after in reserve:
            cnt += 1
            reserve.remove(after)
                    
    return n - (len(lost) - cnt)
            

        