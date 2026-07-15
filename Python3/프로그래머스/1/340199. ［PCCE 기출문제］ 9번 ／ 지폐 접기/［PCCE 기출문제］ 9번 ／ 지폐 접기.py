def solution(wallet, bill):

    wallet, bill = sorted(wallet), sorted(bill)
    cnt = 0
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[-1] //= 2
        bill = sorted(bill)
        cnt += 1

    return cnt