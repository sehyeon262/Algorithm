def solution(nums):
    N = len(set(nums))  #
    num = len(nums) // 2
    
    if N < num:
        return N
    else:
        return num
    
    
    
#     num = N / 2   # 가질 수 있는 포켓몬 수
    
#     now = nums[0]   # 현재 선택된 포켓몬 종류
#     for i in range(1, N):
#         if nums[i] == now:
#             continue
#         else:
#             now = nums[i]
#             answer += 1
#             if answer + 1 >= num:
#                 break
                
#     return answer + 1
            
    
