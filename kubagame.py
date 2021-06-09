# usr/bin/env python3
import numpy as np
import sys
# get from commandline the player infos => (PlayerA, black)


def display_instruct():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Kuba Game
    This will be a showdown between your human brain and my silicon processor.
    You will make your move known by entering a number, 0 - 8. The number
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
    )
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
        pass
    def play(self):
        pass
class Board:
    def __init__(self):
        pass
    def draw_board(self):
        pass
    def shift_balls():
        pass
# player_obj = Player()
# player = player_obj.get_player()



if __name__ == "__main__":
    display_instruct()
    