def solution(brown, yellow):
    N = brown + yellow  # 총 격자 개수
    
    # [설명] 가로(row) >= 세로(col) 조건을 만족하려면 세로가 전체 개수의 제곱근을 넘을 수 없습니다.
    # int()를 사용해 소수점을 버림으로써, 제곱근 이하의 안전한 정수 최댓값(마지노선)까지만 탐색하도록 제한합니다.
    # 갈색 테두리가 노란색을 감싸려면 세로는 최소 3 이상이어야 합니다.
    for col in range(3, int(N**0.5) + 1):
        if N % col == 0:
            row = N // col  # 소수점이 없는 정수 나눗셈
            
            # 테두리(brown) 개수 공식이 만족하는지 확인
            if (row + col) * 2 - 4 == brown:
                return [row, col]
