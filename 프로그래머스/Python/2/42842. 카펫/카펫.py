def solution(brown, yellow):
    answer = []
    N = yellow + brown   # 총 격자 개수
    
    # row(가로) >= col(세로)
    # 위 조건에 의해 내림차순으로 반복함
    for row in range(N, 0, -1):
        if N % row == 0:
            col = N / row
            # brown 조건이 일치하다면 (brown이랑 yellow 둘 중 하나의 조건만 일치하면 됨)
            if (row * 2) + (col - 2) * 2 == brown:
                answer.extend([row, col])
                break
    return answer
