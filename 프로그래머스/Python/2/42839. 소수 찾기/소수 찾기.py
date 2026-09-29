from itertools import permutations
from math import sqrt

def solution(numbers):
    nums = []
    
    # 1자리 수부터 모든 길이의 순열을 구해야함.
    for i in range(1, len(numbers) + 1):
        for item in permutations(numbers, i):
            nums.append(int(''.join(item)))
    
    # 중요!!! -> 중복을 제거해야함!!
    nums = set(nums)
    
    cnt = 0
    for a in nums:
        # 0과 1은 소수가 아님.
        if a < 2:
            continue
            
        # 제곱근까지만 나눠서 확인해본다.
        is_prime = True
        for i in range(2, int(sqrt(a)) + 1):
            
            # 나누어 떨어지면 소수가 아님
            if a % i == 0:
                is_prime = False
                break
                
        # 나누어 떨어지지 않으면 소수 -> +1
        if is_prime:
            cnt += 1
            
    return cnt
    