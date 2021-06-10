# !usr/bin/env python3
import numpy as np
import sys
import pandas as pd

def display_instruct():
    """Display game instructions."""
    return 
    """
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
        if self.playerA[1] == 'black':
            return self.playerA[0] +' is black' + self.playerB[0] + f' is {self.playerB[1]}'
        elif self.playerA[1] == self.playerB[1]:
            raise Exception('Both players can\'t have same color')
        else:
            return self.playerA[0] + f' is {self.playerA[1]} \n' + self.playerB[0] + f' is {self.playerB[1]}'
        # if self.playerB[1] == 'white':
        #     return self.playerB[0] +' is white'
        # else:
        #     return self.playerB[0] + f' is {self.playerB[1]}'
        return "Welcome to Kuba Game ..."
class Balls:
    def __init__(self):
        self.white = 'W'
        self.black = 'B'
        self.red ='R'
    def balls(self):
        # no == empty slot
        self.arr = np.array(
            [['w1','w2','no ','no ','no ','B1','B2'],
            ['w3', 'w4','no ','R1 ','no ','B3','B4'],
            ['no', 'no','R2 ','R3 ','R4 ','no','no'],
            ['no', 'R5','R6 ','R7 ','R8 ','R9','no'],
            ['no', 'no','R10','R11','R12','no','no'],
            ['B5', 'B6','no ','R13','no ','W5','W6'],
            ['B7', 'B8','no ','no ','no ','W7','W8']]
        )
        # fill dictionary with array values
        self.ball_dict = {
            'W1': 'white',
            'W2': 'white',
            'W3': 'white',
            'W4': 'white',
            'W5': 'white',
            'W6': 'white',
            'W7': 'white',
            'W8': 'white',
            'B1': 'black',
            'B2': 'black',
            'B3': 'black',
            'B4': 'black',
            'B5': 'black',
            'B6': 'black',
            'B7': 'black',
            'B8': 'black',
            'R1': 'red',
            'R2': 'red',
            'R3': 'red',
            'R4': 'red',
            'R5': 'red',
            'R6': 'red',
            'R7': 'red',
            'R8': 'red',
            'R9': 'red',
            'R10': 'red',
            'R11': 'red',
            'R12': 'red',
            'R13': 'red',
            'no':  '-'

        

        }
        # pandas initializer

        return self.ball_dict
class Board(Balls):
    def __init__(self):
        Balls.__init__(self)
        Balls.balls(self)
    def draw_board(self):
        string = ' | '
        return string.join(self.arr[0]).upper() + '\n' + string.join(self.arr[1]).upper() + '\n' +string.join(self.arr[2]).upper() + '\n' + string.join(self.arr[3]).upper() + '\n' + string.join(self.arr[4]).upper() + '\n' + string.join(self.arr[5]).upper() + '\n' + string.join(self.arr[6]).upper()
    def shift_balls(self):
        # only method left
        ball = input("Enter ball to move...")
        # move = input("Enter direction to move towards (up/down)...")
        # moves = input("Enter number of moves...")
        if ball == 'w1'.upper() or ball == 'w1':
            # if self.arr[0][0]:
            return self.arr[0][0]
        # return self.ball_dict['W1']
        
        

if __name__ == "__main__":
    # try:
    #     player_obj = Player()
    #     player = player_obj.get_player()
    #     print(player)
    # except IndexError as err:
    #     print("run example\n'python kubagame.py ken,black mary,white'")

    player_obj = Board()
    player = player_obj.shift_balls()
    print(player)
    
    