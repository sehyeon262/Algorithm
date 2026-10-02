# 목표 : 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 회원등록 날짜의 총 일수 구하기
# 입력 : 제품들, 제품들의 수량, 할인 제품 배열
# 출력 : 가능한 회원등록 날짜의 총 일수
# 알고리즘 후보 : 완전탐색

def solution(want, number, discount):
    answer = 0
    
    for start in range(len(discount) - 9):
        # 각 시작일은 독립적인 가입 시도니깐 매번 원래 수량으로 시작해야함.
        remaining = number[:]
        cnt = 0
        for cur in range(start, 10 + start):
            for i in range(len(want)):            
                # 같은 과일이 존재하고 number[j]가 0이 아니라면
                if discount[cur] == want[i] and remaining[i] != 0:
                    remaining[i] -= 1
                    cnt += 1
        
        # 10일 모두 할인 받을 수 있다면 +1
        if cnt == 10:
            answer += 1
    
    return answer