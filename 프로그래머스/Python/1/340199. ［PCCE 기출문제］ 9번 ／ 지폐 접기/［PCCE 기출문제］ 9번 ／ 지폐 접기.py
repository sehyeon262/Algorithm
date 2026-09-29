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

# ---------------------------------
# 더 쉬운 풀이

# def solution(wallet, bill):

#    wallet, bill = sorted(wallet), sorted(bill)
#    cnt = 0
#    while wallet[0] < bill[0] or wallet[1] < bill[1]:
#        bill[-1] //= 2
#        bill = sorted(bill)
#        cnt += 1

#    return cnt
