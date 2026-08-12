def solution(nums):
    N = len(set(nums)) 
    num = len(nums) // 2
    
    if N < num:
        return N
    else:
        return num
            
