import pygame


class Pawn:
    def __init__(self, colour):
        self.name = colour + ' pawn'
        self.colour = colour
        self.initial = True
        self.en_passant = False
        if self.colour == 'white':
            self.image = pygame.image.load('images/white pawn.png')
        else:
            self.image = pygame.image.load('images/black pawn.png')

    def check_moves(self, row, column, board):
        moves = []
        if self.colour == 'white':
            if self.initial and not (board[row - 1][column] or board[row - 2][column]):
                moves.append((row - 2, column))
            if not board[row - 1][column]:
                moves.append((row - 1, column))
            if column - 1 >= 0 and board[row - 1][column - 1] and board[row - 1][column - 1].colour == 'black':
                moves.append((row - 1, column - 1))
            if column + 1 < len(board) and board[row - 1][column + 1] and board[row - 1][column + 1].colour == 'black':
                moves.append((row - 1, column + 1))
        else:
            if self.initial:
                moves.append((row + 2, column))
            if not board[row + 1][column]:
                moves.append((row + 1, column))
            if column - 1 >= 0 and board[row + 1][column - 1] and board[row + 1][column - 1].colour == 'white':
                moves.append((row + 1, column - 1))
            if column + 1 < len(board) and board[row + 1][column + 1] and board[row + 1][column + 1].colour == 'white':
                moves.append((row + 1, column + 1))
        return moves


class Rook:
    def __init__(self, colour):
        self.name = colour + ' rook'
        self.colour = colour
        self.initial = True
        if self.colour == 'white':
            self.image = pygame.image.load('images/white rook.png')
        else:
            self.image = pygame.image.load('images/black rook.png')

    def check_moves(self, row, column, board):
        moves = []
        left = right = up = down = True
        for i in range(1, 8):
            if up and row - i >= 0:
                if board[row - i][column]:
                    up = False
                if not board[row - i][column] or board[row - i][column].colour != self.colour:
                    moves.append((row - i, column))

            if down and row + i < len(board):
                if board[row + i][column]:
                    down = False
                if not board[row + i][column] or board[row + i][column].colour != self.colour:
                    moves.append((row + i, column))

            if left and column - i >= 0:
                if board[row][column - i]:
                    left = False
                if not board[row][column - i] or board[row][column - i].colour != self.colour:
                    moves.append((row, column - i))

            if right and column + i < len(board):
                if board[row][column + i]:
                    right = False
                if not board[row][column + i] or board[row][column + i].colour != self.colour:
                    moves.append((row, column + i))

        return moves


class Knight:
    def __init__(self, colour):
        self.name = colour + ' knight'
        self.colour = colour
        if self.colour == 'white':
            self.image = pygame.image.load('images/white knight.png')
        else:
            self.image = pygame.image.load('images/black knight.png')

    def check_moves(self, row, column, board):
        moves = []
        if row + 2 < 8:
            if column + 1 < 8:
                if not board[row + 2][column + 1] or board[row + 2][column + 1].colour != self.colour:
                    moves.append((row + 2, column + 1))
            if column - 1 >= 0:
                if not board[row + 2][column - 1] or board[row + 2][column - 1].colour != self.colour:
                    moves.append((row + 2, column - 1))
        if row - 2 >= 0:
            if column + 1 < 8:
                if not board[row - 2][column + 1] or board[row - 2][column + 1].colour != self.colour:
                    moves.append((row - 2, column + 1))
            if column - 1 >= 0:
                if not board[row - 2][column - 1] or board[row - 2][column - 1].colour != self.colour:
                    moves.append((row - 2, column - 1))
        if column + 2 < 8:
            if row + 1 < 8:
                if not board[row + 1][column + 2] or board[row + 1][column + 2].colour != self.colour:
                    moves.append((row + 1, column + 2))
            if row - 1 < 8:
                if not board[row - 1][column + 2] or board[row - 1][column + 2].colour != self.colour:
                    moves.append((row - 1, column + 2))
        if column - 2 >= 0:
            if row + 1 < 8:
                if not board[row + 1][column - 2] or board[row + 1][column - 2].colour != self.colour:
                    moves.append((row + 1, column - 2))
            if row - 1 < 8:
                if not board[row - 1][column - 2] or board[row - 1][column - 2].colour != self.colour:
                    moves.append((row - 1, column - 2))
        return moves


class Bishop:
    def __init__(self, colour):
        self.name = colour + ' bishop'
        self.colour = colour
        if self.colour == 'white':
            self.image = pygame.image.load('images/white bishop.png')
        else:
            self.image = pygame.image.load('images/black bishop.png')

    def check_moves(self, row, column, board):
        moves = []
        upleft = upright = downleft = downright = True
        for i in range(1, 8):
            if row - i >= 0 and column - i >= 0:

                if upleft and row - i >= 0 and column - i >= 0:
                    if not board[row - i][column - i] or board[row - i][column - i].colour != self.colour:
                        moves.append((row - i, column - i))
                    if board[row - i][column - i]:
                        upleft = False

            if row - i >= 0 and column + i < 8:

                if upright and row - i >= 0 and column + i < 8:
                    if not board[row - i][column + i] or board[row - i][column + i].colour != self.colour:
                        moves.append((row - i, column + i))
                    if board[row - i][column + i]:
                        upright = False

            if row + i < 8 and column - i >= 0:

                if downleft and column - i >= 0 and row + i < 8:
                    if not board[row + i][column - i] or board[row + i][column - i].colour != self.colour:
                        moves.append((row + i, column - i))
                    if board[row + i][column - i]:
                        downleft = False

            if row + i < 8 and column + i < 8:

                if downright and column + i < len(board) and row + i < 8:
                    if not board[row + i][column + i] or board[row + i][column + i].colour != self.colour:
                        moves.append((row + i, column + i))
                    if board[row + i][column + i]:
                        downright = False

        return moves


class Queen:
    def __init__(self, colour):
        self.name = colour + ' queen'
        self.colour = colour
        if self.colour == 'white':
            self.image = pygame.image.load('images/white queen.png')
        else:
            self.image = pygame.image.load('images/black queen.png')

    def check_moves(self, row, column, board):
        moves = []
        left = right = up = down = True
        upleft = upright = downleft = downright = True
        for i in range(8):
            if up and row - i >= 0:
                if not board[row - i][column] or board[row - i][column].colour != self.colour:
                    moves.append((row - i, column))
                    if board[row - i][column]:
                        up = False
            if down and row + i < len(board):
                if not board[row + i][column] or board[row + i][column].colour != self.colour:
                    moves.append((row + i, column))
                    if board[row + i][column]:
                        down = False
            if left and column - i >= 0:
                if not board[row][column - i] or board[row][column - i].colour != self.colour:
                    moves.append((row, column - i))
                    if board[row][column - i]:
                        left = False
            if right and column + i < len(board):
                if not board[row][column + i] or board[row][column + i].colour != self.colour:
                    moves.append((row, column + i))
                    if board[row][column + i]:
                        right = False

            if upleft and row - i >= 0 and column - i >= 0:
                if not board[row - i][column - i] or board[row - i][column - i].colour != self.colour:
                    moves.append((row - i, column - i))
                    if board[row - i][column - i]:
                        upleft = False
            if upright and row - i >= 0 and column + i < 8:
                if not board[row - i][column + i] or board[row - i][column + i].colour != self.colour:
                    moves.append((row - i, column + i))
                    if board[row - i][column + i]:
                        upright = False
            if downleft and column - i >= 0 and row + i < 8:
                if not board[row + i][column - i] or board[row + i][column - i].colour != self.colour:
                    moves.append((row + i, column - i))
                    if board[row + i][column - i]:
                        downleft = False
            if downright and column + i < len(board) and row + i < 8:
                if not board[row + i][column + i] or board[row + i][column + i].colour != self.colour:
                    moves.append((row + i, column + i))
                    if board[row + i][column + i]:
                        downright = False
        return moves


class King:
    def __init__(self, colour):
        self.name = colour + ' king'
        self.colour = colour
        self.initial = True
        self.checked = False
        if self.colour == 'white':
            self.image = pygame.image.load('images/white king.png')
        else:
            self.image = pygame.image.load('images/black king.png')

    def check_moves(self, row, column, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < 8 and 0 <= column + j < 8:
                    if not board[row + i][column + j] or board[row + i][column + j].colour != self.colour:
                        moves.append((row + i, column + j))
        return moves
