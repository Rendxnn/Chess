import window
import pygame
import sys
import pieces
import movement as move


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
        print(board[0][4].check_checks(0, 4, board))
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
            last = False
            board, turn = move.make_move(board, selected, row, column, turn)

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
