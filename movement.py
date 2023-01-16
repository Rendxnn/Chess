import pieces


def check_all_possible(board, colour):
    possible_moves = {}
    for row in range(8):
        for column in range(8):
            if board[row][column] and board[row][column].colour == colour:
                possible_moves[(row, column)] = board[row][column].check_moves(row, column)
    return possible_moves


def make_move(board, selected, row, column, turn):
    if board[selected[0]][selected[1]] and board[row][column] and type(
            board[selected[0]][selected[1]]) == pieces.King and type(board[row][column]) == pieces.Rook and \
            board[selected[0]][selected[1]].colour == board[row][column].colour and row == selected[0]:
        board, turn = castle(board, selected, row, column, turn)

    elif board[selected[0]][selected[1]] and (row, column) in board[selected[0]][selected[1]].check_moves(
            selected[0], selected[1], board):
        if board[selected[0]][selected[1]] and type(board[selected[0]][selected[1]]) in [pieces.Rook,
                                                                                         pieces.King,
                                                                                         pieces.Pawn]:
            board[selected[0]][selected[1]].initial = False
        board[selected[0]][selected[1]], board[row][column] = None, board[selected[0]][selected[1]]
        turn += 1

    return board, turn


def castle(board, selected, row, column, turn):
    if board[selected[0]][selected[1]].check_castle(selected[0], selected[1], board, column):
        if column > selected[1]:
            board[row][selected[1] + 1] = board[row][column]
            board[row][column - 1] = board[row][selected[1]]
            board[row][column] = None
            board[row][selected[1]] = None

            board[row][selected[1] + 1].initial = False
            board[row][column - 1].initial = False

            turn += 1
        elif column < selected[1]:
            board[row][selected[1] - 1] = board[row][column]
            board[row][column + 2] = board[row][selected[1]]
            board[row][column] = None
            board[row][selected[1]] = None

            board[row][selected[1] - 1].initial = False
            board[row][column + 2].initial = False

            turn += 1
    return board, turn
