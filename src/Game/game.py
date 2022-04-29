import json
from .tile import Tile
from .goal import Goal
from .robot import Robot

class Game:
    """ Implement a Ricochet Robot Game"""
    
    def __init__(self, board_file, board_shape:int=16):
        """
        board_shape(int): The number of tiles per line and per column, game is played by default on a 16 by 16 grid
        """
        self.board_shape = board_shape
        self.board_file = board_file
        self.generate_board()
        self.robots = [Robot(c, self) for c in ["R", "Y", "B", "G"]]
        
    def generate_board(self):
        # Create a board of appropriate shape with empty tiles
        self.board = [[Tile() for j in range(self.board_shape)] for i in range(self.board_shape)]
        
        # Create walls on the side of the board
        # Top side walls
        for tile in self.board[0]:
            tile.top_wall = True
        # Bottom side walls
        for tile in self.board[self.board_shape-1]:
            tile.bottom_wall = True
        # Left and right side walls
        for row in self.board:
            row[0].left_wall = True
            row[self.board_shape-1].right_wall = True
            
        # Create walls in the middle square of the board
        tile = self.board[int(self.board_shape/2) - 1][int(self.board_shape/2) - 1]
        tile.left_wall=True
        tile.top_wall=True
        
        tile = self.board[int(self.board_shape/2) - 1][int(self.board_shape/2)]
        tile.right_wall=True
        tile.top_wall=True
        
        tile = self.board[int(self.board_shape/2)][int(self.board_shape/2) - 1]
        tile.left_wall=True
        tile.bottom_wall=True
        
        tile = self.board[int(self.board_shape/2)][int(self.board_shape/2)]
        tile.right_wall=True
        tile.bottom_wall=True
        
        self.apply_board_file()
        
    def apply_board_file(self):
        with open(self.board_file) as f:
            board_elements = json.load(f)
        for (i,j) in board_elements.get("h_walls"):
            self.board[i][j].right_wall = True
        for (j, i) in board_elements.get("v_walls"):
            self.board[i+1][j].top_wall = True
        for (i, j, color, pattern) in board_elements.get("goals"):
            goal = Goal(color, pattern)
            self.board[i][j].goal = goal


    def update_robot_on_board(self, robot: Robot):
        """Updates a Robot Position on the board."""
        self.board[robot.row][robot.column].robot = robot


    def move_robot(self, robot: Robot, direction: str):
        """Moves a robot along the according axis until it hits an obstacle."""
        if direction == "left":
            col = robot.column
            while not self.board[robot.row][col].left_wall and col > 0 and (not
                    self.board[robot.row][col-1].right_wall):
                col -= 1
            self.board[robot.row][robot.column].robot = None
            robot.column = col
        elif direction == "right":
            col = robot.column
            while not self.board[robot.row][col].right_wall and (col <
                    self.board_shape) and (not
                            self.board[robot.row][col+1].left_wall):
                col += 1
            self.board[robot.row][robot.column].robot = None
            robot.column = col
        elif direction == "up":
            row = robot.row
            while (not self.board[row][robot.column].top_wall and row > 0 and
            (not self.board[row-1][robot.column].bottom_wall)):
                row -= 1
            self.board[robot.row][robot.column].robot = None
            robot.row = row
        else:  # then we go down.
            row = robot.row
            while (not self.board[row][robot.column].bottom_wall and row <
                    self.board_shape and not
                    self.board[row+1][robot.column].top_wall):
                row += 1
            self.board[robot.row][robot.column].robot = None
            robot.row = row
        self.update_robot_on_board(robot)



    def display_board(self):
        for row in self.board:
            for tile in row:
                if tile.top_wall:
                    print(' ‾‾ ', end = '')
                else:
                    print('    ', end = '')
            
            print('')
            
            for tile in row: 
                if tile.left_wall:
                    print('|', end = '')
                else:
                    print(' ', end = '')
                    
                if tile.goal:
                    print(f'{tile.goal.name}', end='')
                elif tile.robot:
                    print(f'R{tile.robot.color}', end='')
                else:
                    print('  ', end = '')
                
                if tile.right_wall:
                    print('|', end = '')
                else:
                    print(' ', end = '')
                    
            print('')
            
            for tile in row:
                if tile.bottom_wall:
                    print(' __ ', end = '')
                else:
                    print('    ', end = '')   
            print('')
