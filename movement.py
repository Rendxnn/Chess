import pieces
import window


def make_move(board, selected, row, column, turn_counter, players):
    current_board = [r.copy() for r in board]
    current_king = players[turn_counter % 2].king
    if board[selected[0]][selected[1]] and board[row][column] and type(
            board[selected[0]][selected[1]]) == pieces.King and type(board[row][column]) == pieces.Rook and \
            board[selected[0]][selected[1]].colour == board[row][column].colour and row == selected[0]:
        board, turn_counter, players = castle(board, selected, row, column, turn_counter, players)

    elif (row, column) in board[selected[0]][selected[1]].check_moves(selected[0], selected[1], board) and type(
            board[selected[0]][selected[1]]) == pieces.Pawn and (
            (row == 0 and board[selected[0]][selected[1]].colour == 'white') or (
            row == 7 and board[selected[0]][selected[1]].colour == 'black')):
        board[selected[0]][selected[1]], board[row][column] = None, board[selected[0]][selected[1]]
        prom = window.display_promotion(board[row][column].colour)
        board[row][column] = prom
        turn_counter += 1

    elif board[selected[0]][selected[1]] and (row, column) in board[selected[0]][selected[1]].check_moves(
            selected[0], selected[1], board):
        if type(board[selected[0]][selected[1]]) in [pieces.Rook, pieces.King, pieces.Pawn]:
            if board[selected[0]][selected[1]].initial:
                board[selected[0]][selected[1]].initial = False
            if type(board[selected[0]][selected[1]]) == pieces.King:
                print('moved king')
                players[turn_counter % 2].king = (row, column)
            if type(board[selected[0]][selected[1]]) == pieces.Pawn and row == selected[0] + 2:
                board[selected[0]][selected[1]].en_passant = turn_counter

        board[selected[0]][selected[1]], board[row][column] = None, board[selected[0]][selected[1]]
        turn_counter += 1
    kingx, kingy = players[(turn_counter - 1) % 2].king
    if board[kingx][kingy].check_checks(kingx, kingy, board):
        board = current_board
        turn_counter -= 1
        players[turn_counter % 2].king = current_king

    return board, turn_counter, players


def castle(board, selected, row, column, turn_counter, players):
    if board[selected[0]][selected[1]].check_castle(selected[0], selected[1], board, column):
        if column > selected[1]:
            players[turn_counter % 2].king = (row, column - 1)
            board[row][selected[1] + 1] = board[row][column]
            board[row][column - 1] = board[row][selected[1]]
            board[row][column] = None
            board[row][selected[1]] = None

            board[row][selected[1] + 1].initial = False
            board[row][column - 1].initial = False

            turn_counter += 1
        elif column < selected[1]:
            players[turn_counter % 2].king = (row, column + 2)
            board[row][selected[1] - 1] = board[row][column]
            board[row][column + 2] = board[row][selected[1]]
            board[row][column] = None
            board[row][selected[1]] = None

            board[row][selected[1] - 1].initial = False
            board[row][column + 2].initial = False

            turn_counter += 1
    return board, turn_counter, players


def en_passant(selected, row, column, board):
    pass
