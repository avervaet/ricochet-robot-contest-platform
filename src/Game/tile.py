from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .robot import Robot
    from .goal import Goal

class Tile:
    
    def __init__(self, robot:Robot=None, goal:Goal=None):
        """
        robot(Robot): Indicates if a robot is present on the tile, and refers to it if so
        goal(Goal): Indicates if a goal is present on the tile, and refers to if if so
        """
        self.robot = robot
        self.goal = goal
        
        # By default a doesnt have walls
        self.left_wall = False
        self.right_wall = False
        self.top_wall = False
        self.bottom_wall =False
