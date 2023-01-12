import pygame

pygame.init()


def display(board):
    size = 480, 480
    window = pygame.display.set_mode(size)
    board_img = pygame.image.load('board.png')
    window.blit(board_img, (0, 0))
    for row in range(len(board)):
        for piece in range(len(board[row])):
            if board[row][piece]:
                window.blit(board[row][piece].image, (piece * 60, row * 60))
    pygame.display.update()




