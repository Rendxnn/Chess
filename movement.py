import pieces
import window


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

    elif (row, column) in board[selected[0]][selected[1]].check_moves(selected[0], selected[1], board) and type(
            board[selected[0]][selected[1]]) == pieces.Pawn and (
            (row == 0 and board[selected[0]][selected[1]].colour == 'white') or (
            row == 7 and board[selected[0]][selected[1]].colour == 'black')):
        board[selected[0]][selected[1]], board[row][column] = None, board[selected[0]][selected[1]]
        prom = window.display_promotion(board[row][column].colour)
        board[row][column] = prom
        turn += 1

    elif board[selected[0]][selected[1]] and (row, column) in board[selected[0]][selected[1]].check_moves(
            selected[0], selected[1], board):
        if board[selected[0]][selected[1]] and type(board[selected[0]][selected[1]]) in [pieces.Rook,
                                                                                         pieces.King,
                                                                                         pieces.Pawn] and \
                board[selected[0]][selected[1]].initial:
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


def promotion(board, selected, row, column, turn):
    pass


