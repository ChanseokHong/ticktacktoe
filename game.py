# import pygame
# import tkinter
from exam import aexam
from exam import bexam
from exam import exam
from ai import aiwin
from ai import ailose
from ai import airandom
# #delet after test
# mode = 0
#
# monitor_height = root.winfo_screenheight()
# monitor_width = root.winfo_screenwidth()
#
# screensize = (monitor_hight * 2) / 3
#
# pygame, init()
# pygame.display.set_caption('Tick-Tack_Toe')
# displaysurf = pygame.display.set_mode((screensize, screensize), 0, 32)\

tiles = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def game():
    turn = 0
    awin = False
    bwin = False
    draw = False
    while awin is False and bwin is False and draw is False:
        showinterface()
        value = False
        if turn % 2 == 0:
            while value is False:
                value = playturn(1)
        else:
            while value is False:
                value = aiturn(0)
        awin = aexam(tiles)
        bwin = bexam(tiles)
        draw = exam(tiles)
        if awin is True:
            showinterface()
            print("X win!")
        if bwin is True:
            showinterface()
            print("O win!")
        if draw is True:
            showinterface()
            print("Draw")
        turn += 1


def playturn(player):
    print(playertosign(player) + " turn")
    try:
        x, y = input().split(",")
    except ValueError:
        return False
    x = int(x) - 1
    y = int(y) - 1
    if tiles[x][y] == " ":
        tiles[x][y] = playertosign(player)
        return True
    else:
        return False


def aiturn(player):
    x, y = aiwin(tiles).split(",")
    x, y = ailose(tiles).split(",")
    x, y = airandom(tiles).split(",")
    if tiles[x][y] == " ":
        tiles[x][y] = playertosign(player)
        return True
    else:
        return False


def playertosign(player):
    if player == 0:
        return "O"
    return "X"


def showinterface():
    print("┏━━━1━━━┳━━━2━━━┳━━━3━━━┓")
    print("┃       ┃       ┃       ┃ ")
    print("1   " + str(tiles[0][0]) + "   ┃   "
          + str(tiles[0][1]) + "   ┃   " + str(tiles[0][2]) + "   ┃")
    print("┃       ┃       ┃       ┃")
    print("┣━━━━━━━╋━━━━━━━╋━━━━━━━┫")
    print("┃       ┃       ┃       ┃")
    print("2   " + str(tiles[1][0]) + "   ┃   "
          + str(tiles[1][1]) + "   ┃   " + str(tiles[1][2]) + "   ┃")
    print("┃       ┃       ┃       ┃")
    print("┣━━━━━━━╋━━━━━━━╋━━━━━━━┫")
    print("┃       ┃       ┃       ┃")
    print("3   " + str(tiles[2][0]) + "   ┃   "
          + str(tiles[2][1]) + "   ┃   " + str(tiles[2][2]) + "   ┃")
    print("┃       ┃       ┃       ┃")
    print("┗━━━━━━━┻━━━━━━━┻━━━━━━━┛")
