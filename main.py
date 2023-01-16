import window
import pygame
import sys
import pieces


def main():
    board = initialize_board()
    selected = None
    last = False
    turn = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.display(board)
        clicked = pygame.mouse.get_pressed(3)[0]

        if (clicked and not last) or not selected or not board[selected[0]][selected[1]]:
            position = pygame.mouse.get_pos()
            row = position[1] // 60
            column = position[0] // 60
            selected = row, column
            last = clicked

        if not clicked and last and board[selected[0]][selected[1]] and (
                (turn % 2 != 0 and board[selected[0]][selected[1]].colour == 'white') or (
                turn % 2 == 0 and board[selected[0]][selected[1]].colour == 'black')):
            position = pygame.mouse.get_pos()
            row = position[1] // 60
            column = position[0] // 60
            if board[selected[0]][selected[1]] and board[row][column] and type(
                    board[selected[0]][selected[1]]) == pieces.King and type(board[row][column]) == pieces.Rook and \
                    board[selected[0]][selected[1]].colour == board[row][column].colour and row == selected[0]:
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

            elif board[selected[0]][selected[1]] and (row, column) in board[selected[0]][selected[1]].check_moves(
                    selected[0], selected[1], board):
                if board[selected[0]][selected[1]] and type(board[selected[0]][selected[1]]) in [pieces.Rook,
                                                                                                 pieces.King,
                                                                                                 pieces.Pawn]:
                    board[selected[0]][selected[1]].initial = False
                board[selected[0]][selected[1]], board[row][column] = None, board[selected[0]][selected[1]]
                turn += 1
            selected = None
            last = False
        elif not clicked and last:
            selected = None
            last = False


def initialize_board():
    board = [([None] * 8) for _ in range(8)]
    order = [pieces.Rook, pieces.Knight, pieces.Bishop, pieces.Queen,
             pieces.King, pieces.Bishop, pieces.Knight, pieces.Rook]

    for piece in range(8):
        board[7][piece] = order[piece]('white')
        board[6][piece] = pieces.Pawn('white')

        board[1][piece] = pieces.Pawn('black')
        board[0][piece] = order[piece]('black')

    return board


main()
