def solution(clothes):
    answer = 1
    types = {}
    
    for name, kind in clothes:
        # types 안에 kind가 있으면 그 값을 가져오고, 없으면 0으로 시작해라.
        types[kind] = types.get(kind, 0) + 1
        
    # dict에서 값만 꺼냄
    for a in types.values():
        # 종류별 옷 개수 + 해당 옷을 안 입는 경우 1개
        answer *= a + 1
    
    # 모든 옷 안 입는 경우 뺌
    return answer - 1