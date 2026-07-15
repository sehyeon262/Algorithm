# 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다. 
# 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다. => round()
# 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다. => 길이가 둘 다 작으면 그만!

def solution(wallet, bill):
    answer = 0
    
    wallet.sort()
    bill.sort()
    
    while (bill[0] > wallet[0] or bill[1] > wallet[1]):
        if bill[0] > bill[1]:
            bill[0] //= 2
            answer += 1
        else:
            bill[1] //= 2
            answer += 1
        wallet.sort()
        bill.sort()
        
    
    return answer