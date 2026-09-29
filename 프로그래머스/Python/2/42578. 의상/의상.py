def solution(clothes):
    types = {}
    
    for name, kind in clothes:
        # 같은 종류가 없으면 +2 (입는 경우 + 안입는 경우) 
        if kind not in types:
            types[kind] = 2
        # 같은 종류 있으면 +1 (입는 경우) -> 안 입는 경우는 이미 들어가 있으니깐
        else:
            types[kind] += 1
    
    res = 1
    # 종류들의 경우의 수 세기
    for a in types.values():
        res *= a
    
    # 모든 종류의 옷 다 안 입는 경우 빼기
    return res - 1


# def solution(clothes):
#     answer = 1
#     types = {}
    
#     for name, kind in clothes:
#         # types 안에 kind가 있으면 그 값을 가져오고, 없으면 0으로 시작해라.
#         types[kind] = types.get(kind, 0) + 1
        
#     # dict에서 값만 꺼냄
#     for a in types.values():
#         # 종류별 옷 개수 + 해당 옷을 안 입는 경우 1개
#         answer *= a + 1
    
#     # 모든 옷 안 입는 경우 뺌
#     return answer - 1
