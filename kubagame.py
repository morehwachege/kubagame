# !usr/bin/env python3
import numpy as np
import sys
import pandas as pd

def display_instruct():
    """Display game instructions."""

    return  """
                Welcome to the greatest intellectual challenge of all time: Kuba Game
                This will be a showdown between your human brain and my silicon processor.
                You will make your move known by entering a number, 0-49. The number
                will corresponde to the board position as illustrated:
                                W | W | - | - | - | B | B |
                                ---------------------------
                                W | W | - | R | - | B | B |
                                ---------------------------
                                - | - | R | R | R | - | - |
                                ---------------------------
                                - | R | R | R | R | R | - |
                                ---------------------------
                                - | - | R | R | R | - | - |
                                ---------------------------
                                B | B | - | R | - | W | W |
                                ---------------------------
                                B | B | - | - | - | W | W |
                                ---------------------------
                Prepare yourself, human. The ultimate battle is about to begin. \n
            """
class Player:
    def __init__(self):
        self.playerA = sys.argv[1]
        self.playerB = sys.argv[2]
    def get_player(self):
        self.playerA = self.playerA.split(',')
        self.playerB = self.playerB.split(',')
        
        if self.playerA[1] == self.playerB[1]:
            raise Exception('Both players can\'t have same color')
        else:
            return self.playerA[0] + f' is {self.playerA[1]} \n' + self.playerB[0] + f' is {self.playerB[1]}'
        # if self.playerB[1] == 'white':
        #     return self.playerB[0] +' is white'
        # else:
        #     return self.playerB[0] + f' is {self.playerB[1]}'
        return "Welcome to Kuba Game ..."
    def play(self):
        # self.turn = f"It's {"
        pass
class Balls:
    def __init__(self):
        self.white = 'W'
        self.black = 'B'
        self.red ='R'
    def balls(self):
        # no == empty slot
        self.arr = np.array(
            [['w1','w2','-- ','-- ','-- ','B1','B2'],
            ['w3', 'w4','-- ','R1 ','-- ','B3','B4'],
            ['--', '--','R2 ','R3 ','R4 ','--','--'],
            ['--', 'R5','R6 ','R7 ','R8 ','R9','--'],
            ['--', '--','R10','R11','R12','--','--'],
            ['B5', 'B6','-- ','R13','-- ','W5','W6'],
            ['B7', 'B8','-- ','-- ','-- ','W7','W8']]
        )
        self.ball_dict = {
            'W1': self.arr[0][0],
            'W2': self.arr[0][1],
            'W3': self.arr[1][0],
            'W4': self.arr[1][1],
            'W5': self.arr[5][5],
            'W6': self.arr[5][6],
            'W7': self.arr[6][5],
            'W8': self.arr[6][6],
            'B1': self.arr[0][5],
            'B2': self.arr[0][6],
            'B3': self.arr[1][5],
            'B4': self.arr[1][6],
            'B5': self.arr[5][0],
            'B6': self.arr[5][1],
            'B7': self.arr[6][0],
            'B8': self.arr[6][1],
            'R1': self.arr[1][3],
            'R2': self.arr[2][2],
            'R3': self.arr[2][3],
            'R4': self.arr[2][4],
            'R5': self.arr[3][1],
            'R6': self.arr[3][2],
            'R7': self.arr[3][3],
            'R8': self.arr[3][4],
            'R9': self.arr[3][5],
            'R10': self.arr[4][2],
            'R11': self.arr[4][3],
            'R12': self.arr[4][4],
            'R13': self.arr[5][3],
            'no':  '--'

        

        }
        return self.ball_dict
class Board(Balls):
    """
    This is the board class for the balls and moving the elements. Also contains most of the logic
    """
    def __init__(self):
        Balls.__init__(self)
        Balls.balls(self)
    def draw_board(self):
        string = ' | '
        return string.join(self.arr[0]).upper() + '\n' + string.join(self.arr[1]).upper() + '\n' +string.join(self.arr[2]).upper() + '\n' + string.join(self.arr[3]).upper() + '\n' + string.join(self.arr[4]).upper() + '\n' + string.join(self.arr[5]).upper() + '\n' + string.join(self.arr[6]).upper()
    def shift_balls(self):
        # only method left
        # ball = input("Enter ball to move...")
        # direction = input("Enter direction to move towards (up/down/left/right)...")
        # moves = int(input("Enter number of moves..."))
        if ball == 'w1'.upper() or ball == 'w1':
            # if self.arr[0][0]:
            if direction == 'down':
                # if moves == 1:
                if self.arr[1][0] != '--':
                    self.arr[2][0] = self.arr[2][0].replace(self.arr[2][0],self.arr[1][0])
                    self.arr[1][0] = self.arr[1][0].replace(self.arr[1][0], self.arr[0][0])
                    self.arr[0][0] = self.arr[0][0].replace(self.arr[0][0], self.ball_dict['no'])
                    return  self.arr
                
            if direction == 'right':
                if self.arr[1][0] != '--' or self.arr[1][0] != 'no':
                    self.arr[0][2] = self.arr[0][2].replace(self.arr[0][2],self.arr[0][1])
                    self.arr[0][1] = self.arr[0][1].replace(self.arr[0][1], self.arr[0][0])
                    self.arr[0][0] = self.arr[0][0].replace(self.arr[0][0], self.ball_dict['no'])
                    return self.arr
            if direction == 'up' or direction == 'left':
                return "It can't move that way right now :0 ....."
                
# more directions
        
        
        

if __name__ == "__main__":
    # try:
    #     player_obj = Player()
    #     player = player_obj.get_player()
    #     print(player)
    # except IndexError as err:
    #     print("run example\n'python kubagame.py ken,black mary,white'")
    player_obj = Player()
    first_player = player_obj.playerA.split(',')[0].capitalize()
    print(display_instruct())
    print(f"""
    Player {first_player} begins the play
    """)
    mover_obj = Board()
    running = True
    while running:
        ball = input("Enter ball to move...")
        direction = input("Enter direction to move towards (up/down/left/right)...")
        mover = mover_obj.shift_balls()
        print(mover)
        # running = False
    
    
    # player = player.play()
    print(mover)