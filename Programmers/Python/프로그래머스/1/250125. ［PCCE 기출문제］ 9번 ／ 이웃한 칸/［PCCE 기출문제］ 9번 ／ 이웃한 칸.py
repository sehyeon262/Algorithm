def solution(board, h, w):
    answer = 0
    n = len(board)
    
    dir_x = [-1, 1, 0, 0]
    dir_y = [0, 0, -1, 1]
    
    color = board[h][w]

    for i in range(4):
        dx = h + dir_x[i]
        dy = w + dir_y[i]
        if 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy] == color:
                answer += 1
                
    return answer