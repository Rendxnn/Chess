import window
import pygame
import sys
import pieces
import movement as move
import player


def main():
    board = initialize_board()
    selected = None
    last = False
    players = [player.Player("white"), player.Player('bLack')]
    turn_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.display(board)
        clicked = pygame.mouse.get_pressed(3)[0]
        if clicked:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, column = mouse_y // 60, mouse_x // 60
            piece = board[row][column]
            white_turn = turn_counter % 2 == 0
            if piece is not None and ((piece.colour == 'white' and white_turn) or piece.colour == 'black' and not white_turn):
                selected_piece = board[row][column]
                last_board = [row.copy() for row in board]
                board[row][column] = None
                while clicked:
                    clicked = pygame.mouse.get_pressed(3)[0]
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    window.display_dragging(board, selected_piece, mouse_x, mouse_y)
                released_x, released_y = pygame.mouse.get_pos()
                row_released, column_released = released_y // 60, released_x // 60
                board, turn_counter, players = move.make_move(last_board, (row, column), row_released, column_released, turn_counter, players)


def initialize_board():
    board = [([None] * 8) for _ in range(8)]
    order = [pieces.Rook, pieces.Knight, pieces.Bishop, pieces.Queen,
             pieces.King, pieces.Bishop, pieces.Knight, pieces.Rook]

    for i in range(8):
        board[7][i] = order[i]('white')
        board[6][i] = pieces.Pawn('white')

        board[1][i] = pieces.Pawn('black')
        board[0][i] = order[i]('black')

    return board


main()

