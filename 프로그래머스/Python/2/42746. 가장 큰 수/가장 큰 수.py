def solution(numbers):
    lst = []
    
    # (4번 반복한 문자열, 원래 문자열) 튜플 형태로 저장
    for num in numbers:
        s = str(num)
        lst.append((s * 4, s))
    
    # 내림차순 정렬
    lst.sort(reverse=True)
    
    # 정렬된 순서대로 원래 문자열(item[1])을 이어 붙임
    res = ''
    for item in lst:
        res += item[1]
    
    # 모든 숫자가 0인 경우 (ex. "000"이 '0'이 되도록 예외처리!!! )
    if res[0] == '0':
        return '0'
    
    return res