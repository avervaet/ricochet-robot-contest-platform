from tile import Tile
from random import randrange

class Robot:
    
    def __init__(self, color:str, board: list[list[Tile]]):
        self.color = color
        self.row, self.column = _find_suitable_coordinates(board)


    def _find_suitable_coordinates(board: list[list[Tile]]):
        suitable_coordinates = False
        while(not suitable_coordinates):
            row = randrange(0, len(board))
            column = randrange(0, len(board[0]))
            # the coordinates must not represent one of the center tiles.
            middle_elems = [int(self.board_shape/2) -1, int(self.board_shape/2)]
            if row in middle_elems or column in middle_elems:
                continue
            # the coordinates must represent a tile that has no robot or goal.
            tile = board[row][column]
            if not tile.robot and not tile.goal:
                suitable_coordinates = True
        return row, column

