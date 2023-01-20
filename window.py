import pygame
import pieces
import sys

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
    pygame.init()
    options = [[pieces.Queen, pieces.Rook], [pieces.Bishop, pieces.Knight]]
    size = 120, 120
    window2 = pygame.display.set_mode(size)
    promotion_board = pygame.image.load('images/promotion board.png')
    window2.blit(promotion_board, (0, 0))
    for row in range(2):
        for column in range(2):
            window2.blit(options[row][column](colour).image, (column * 60, row * 60))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clicked = pygame.mouse.get_pressed(3)[0]
        if clicked:
            position = pygame.mouse.get_pos()
            row = position[1] // 60
            column = position[0] // 60
            return options[row][column](colour)
