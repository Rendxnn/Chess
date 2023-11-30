import pygame


class Pawn:
    def __init__(self, colour):
        self.name = colour + ' pawn'
        self.colour = colour
        self.initial = True
        self.en_Passant = 0
        if self.colour == 'white':
            self.image = pygame.image.load('images/white pawn.png')
        else:
            self.image = pygame.image.load('images/black pawn.png')

    def __str__(self):
        return self.name

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
            if self.initial and board[row + 1][column] is None and board[row + 2][column] is None:
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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

    def check_moves(self, row, column, board):
        moves = []
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                if 0 <= row + i < 8 and 0 <= column + j < 8:
                    if not board[row + i][column + j] or board[row + i][column + j].colour != self.colour:
                        moves.append((row + i, column + j))
                if 0 <= row + j < 8 and 0 <= column + i < 8:
                    if not board[row + j][column + i] or board[row + j][column + i].colour != self.colour:
                        moves.append((row + j, column + i))
        return moves


class Bishop:
    def __init__(self, colour):
        self.name = colour + ' bishop'
        self.colour = colour
        if self.colour == 'white':
            self.image = pygame.image.load('images/white bishop.png')
        else:
            self.image = pygame.image.load('images/black bishop.png')

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

    def check_moves(self, row, column, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < 8 and 0 <= column + j < 8:
                    if not board[row + i][column + j] or board[row + i][column + j].colour != self.colour:
                        moves.append((row + i, column + j))
        return moves

    def check_castle(self, row, column, board, rook_column):
        if self.initial and board[row][rook_column].initial:
            for square in range(min(column, rook_column) + 1, max(column, rook_column)):
                if board[row][square]:
                    return False
            return True
        return False

    def check_checks(self, row, column, board):
        left = right = up = down = True
        upleft = upright = downleft = downright = True
        for i in range(1, 8):
            if up and row - i >= 0:
                if board[row - i][column] and board[row - i][column].colour != self.colour and type(
                        board[row - i][column]) in [Rook, Queen]:
                    return True
                elif board[row - i][column]:
                    up = False
            if down and row + i < len(board):
                if board[row + i][column] and board[row + i][column].colour != self.colour and type(
                        board[row + i][column]) in [Rook, Queen]:
                    return True
                elif board[row + i][column]:
                    down = False
            if left and column - i >= 0:
                if board[row][column - i] and board[row][column - i].colour != self.colour and type(
                        board[row][column - i]) in [Rook, Queen]:
                    return True
                elif board[row][column - i]:
                    left = False
            if right and column + i < len(board):
                if board[row][column + i] and board[row][column + i].colour != self.colour and type(
                        board[row][column + i]) in [Rook, Queen]:
                    return True
                elif board[row][column + i]:
                    right = False

            if upleft and row - i >= 0 and column - i >= 0:
                if board[row - i][column - i] and board[row - i][column - i].colour != self.colour and (
                        type(board[row - i][column - i]) in [Bishop, Queen] or (
                        type(board[row - i][column - i]) == Pawn and i == 1)):
                    return True
                elif board[row - i][column - i] and board[row - i][column - i].colour == self.colour:
                    upleft = False

            if upright and row - i >= 0 and column + i < 8:
                if board[row - i][column + i] and board[row - i][column + i].colour != self.colour and (
                        type(board[row - i][column + i]) in [Bishop, Queen] or (
                        type(board[row - i][column + i]) == Pawn and i == 1)):
                    return True
                elif board[row - i][column + i] and board[row - i][column + i].colour == self.colour:
                    upright = False

            if downleft and column - i >= 0 and row + i < 8:
                if board[row + i][column - i] and board[row + i][column - i].colour != self.colour and (
                        type(board[row + i][column - i]) in [Bishop, Queen] or (
                        type(board[row + i][column - i]) == Pawn and i == 1)):
                    return True
                elif board[row + i][column - i] and board[row + i][column - i].colour == self.colour:
                    downleft = False

            if downright and column + i < len(board) and row + i < 8:
                if board[row + i][column + i] and board[row + i][column + i].colour != self.colour and (
                        type(board[row + i][column + i]) in [Bishop, Queen] or (
                        type(board[row + i][column + i]) == Pawn and i == 1)):
                    return True
                elif board[row + i][column + i] and board[row + i][column + i].colour == self.colour:
                    downright = False

        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                if 0 <= row + i < 8 and 0 <= column + j < 8:
                    if board[row + i][column + j] and board[row + i][column + j].colour != self.colour and type(
                            board[row + i][column + j]) == Knight:
                        return True
                if 0 <= row + j < 8 and 0 <= column + i < 8:
                    if board[row + j][column + i] and board[row + j][column + i].colour != self.colour and type(
                            board[row + j][column + i]) == Knight:
                        return True
        return False
