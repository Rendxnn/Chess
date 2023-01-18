import pygame
import pieces


pygame.init()


def display(board):
    size = 480, 480
    window = pygame.display.set_mode(size)
    board_img = pygame.image.load('images/board.png')
    window.blit(board_img, (0, 0))
    for row in range(len(board)):
        for piece in range(len(board[row])):
            if board[row][piece]:
                window.blit(board[row][piece].image, (piece * 60, row * 60))
    pygame.display.update()


def display_promotion(colour):
    options = [[pieces.Queen, pieces.Rook], [pieces.Bishop, pieces.Knight]]
    size = 120, 120
    window = pygame.display.set_mode(size)
    promotion_board = pygame.image.load('images/promotion board.png')
    window.blit(promotion_board, (0, 0))
    for row in range(2):
        for column in range(2):
            window.blit(options[row][column](colour).image, (column * 60, row * 60))
    pygame.display.update()


display_promotion('white')
