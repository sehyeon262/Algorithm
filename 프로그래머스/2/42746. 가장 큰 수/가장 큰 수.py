def solution(numbers):
    # 1. 숫자 list -> 문자열 list 변환
    lst = list(map(str, numbers))    
    
    # 2. 각 문자열을 4번 반복한 값을 기준으로 내림차순 정렬 (최대 자릿수(4) 만큼 반복)
    lst.sort(key=lambda x: x * 4, reverse=True)
    
    # 3. 정렬된 문자열들을 하나로 붙임
    res = ''.join(lst)
    
    # 4. [0, 0, 0] 같은 경우 "000" 대신 "0"으로 반환함!
    if res[0] == '0':
        return '0'
    
    return res


