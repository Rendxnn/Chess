class Player:
    def __init__(self, colour):
        self.colour = colour
        self.king = (7, 4) if colour == 'white' else (0, 4)
        self.checked = False
