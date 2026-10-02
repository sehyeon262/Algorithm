# 1. Counter로 크기별 귤 개수 구함
# 2. 개수를 내림치순 정렬
# 3. 많은 개수부터 k에서 뺀다.
# 4. k <= 0이 되는 순간까지 사용한 종류 수를 센다.

from collections import Counter

def solution(k, tangerine):
    lst = Counter(tangerine).values()
    lst = sorted(lst, reverse = True)
    
    cnt = 0
    for n in (lst):
        if k <= 0:
            return cnt
        k -= n
        cnt += 1
    return cnt