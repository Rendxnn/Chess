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

        if not clicked and last and board[selected[0]][selected[1]] and ((turn % 2 != 0 and board[selected[0]][selected[1]].colour == 'white') or (turn % 2 == 0 and board[selected[0]][selected[1]].colour == 'black')):
            position = pygame.mouse.get_pos()
            row = position[1] // 60
            column = position[0] // 60
            if board[selected[0]][selected[1]] and (row, column) in board[selected[0]][selected[1]].check_moves(selected[0], selected[1], board):
                if board[selected[0]][selected[1]] and type(board[selected[0]][selected[1]]) == pieces.Pawn:
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

    for piece in range(len(order)):
        board[7][piece] = order[piece]('white')
        board[6][piece] = pieces.Pawn('white')

        board[1][piece] = pieces.Pawn('black')
        board[0][piece] = order[piece]('black')

    for row in board:
        print([piece.name for piece in row if piece])

    return board


main()
