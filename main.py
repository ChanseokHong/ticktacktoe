# import pygame
from game import game
from game import humanplayturn
from game import aieasyturn
from game import ainormalturn
from game import aihardturn

class Player():
  def __init__(self, playTurn):
    self.playTurn = playTurn

def make_player(mode):
    if mode == "1":
        return Player(humanplayturn)
    if mode == "2":
        return Player(aieasyturn)
    if mode == "3":
        return Player(ainormalturn)
    if mode == "4":
        return Player(aihardturn)
    return False

def main():
    player1 = False
    player2 = False
    while player1 is False:
        print("Select first player\n")
        print("1. human 2. easy ai 3. normal ai 4. hard ai")
        pl1mode = input()
        player1 = make_player(pl1mode)
    while player2 is False:
        print("Select second player\n")
        print("1. human 2. easy ai 3. normal ai 4. hard ai")
        pl1mode = input()
        player2 = make_player(pl1mode)
    game(player1,player2)

if __name__ == "__main__":
    main()
