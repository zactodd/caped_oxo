def is_win(board):
    for i in range(3):
        row = board[i]
        if row[0][1] == row[1][1] == row[2][1] is not None or \
            board[0][i][1] == board[1][i][1] == board[2][i][1] is not None:
            return True
    return board[0][0][1] == board[1][1][1] == board[2][2][1] is not None or \
           board[0][2][1] == board[1][1][1] == board[2][0][1] is not None

# def dfs(board=None, turn=0, max_depth=10, depth=0, alpha=-1000000, beta=1000000):
#     if board is None:
#         board = [
#             [(0, None), (0, None), (0, None)],
#             [(0, None), (0, None), (0, None)],
#             [(0, None), (0, None), (0, None)],
#         ]


