def solution(sizes):
    res = 1
    for i in range(len(sizes)):
        sizes[i].sort()
    
    for k in range(2):
        max_num = sizes[0][k]
        for j in range(1, len(sizes)):
            if sizes[j][k] > max_num:
                max_num = sizes[j][k]
                
        res *= max_num
    return res



# --------------다른 풀이 ----------------
# def solution(sizes):
#     row = 0   # 행
#     col = 0   # 열
#     for a, b in sizes:
#         if a < b:   # 정렬
#             a, b = b, a
#         row = max(row, a)
#         col = max(col, b)
#     return row * col
    
