from __future__ import annotations
from random import randrange
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .game import Game

class Robot:
    
    def __init__(self, color:str, game: Game):
        self.color = color
        self.row, self.column = self._find_suitable_coordinates(game)
        game.init_robot_on_board(self)


    def _find_suitable_coordinates(self, game: Game):
        suitable_coordinates = False
        while(not suitable_coordinates):
            row = randrange(0, game.board_shape)
            column = randrange(0, game.board_shape)
            # the coordinates must not represent one of the center tiles.
            middle_elems = [int(game.board_shape/2) -1, int(game.board_shape/2)]
            if row in middle_elems or column in middle_elems:
                continue
            # the coordinates must represent a tile that has no robot or goal.
            tile = game.board[row][column]
            if not tile.robot and not tile.goal:
                suitable_coordinates = True
        return row, column

