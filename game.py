from exam import aexam
from exam import bexam
from exam import exam
from ai import basicai
from ai import airandom
from ai import aihardstart
from ai import aihardsec
import os
import time

tiles = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def game(pl1,pl2):
    turn = 0;awin = False;bwin = False;draw = False
    while awin is False and bwin is False and draw is False:
        showinterface()
        value = False
        if turn % 2 == 0:
            while value is False:
                value = pl1.playTurn(1)
        else:
            while value is False:
                value = pl2.playTurn(0)
        awin = aexam(tiles)
        bwin = bexam(tiles)
        draw = exam(tiles)
        if awin is True:
            showinterface()
            print("X win!")
        if bwin is True:
            showinterface()
            print("O win!")
        if awin is False and bwin is False and draw is True:
            showinterface()
            print("Draw")
        turn += 1


def humanplayturn(player):
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

def aieasyturn(player):
    time.sleep(1)
    random = airandom(tiles)
    tiles[random[0]][random[1]] = playertosign(player)
    return True

def ainormalturn(player):
    time.sleep(1)
    try:
        basic = basicai(tiles,player)
        tiles[basic[0]][basic[1]] = playertosign(player)
        return True
    except:
        random = airandom(tiles)
        tiles[random[0]][random[1]] = playertosign(player)
        return True

def aihardturn(player,tiles,turn):
    time.sleep(1)
    try:
        basic = basicai(tiles,player)
        tiles[basic[0]][basic[1]] = playertosign(player)
        return True
    except:
        if turn == 0:
            start = aihardstart(tiles)
            tiles[start[0]][start[1]] = playertosign(player)
            return True
        elif turn == 1:
            sec = aihardsec(tiles)
            tiles[sec[0]][sec[1]] = playertosign(player)
            return True
        elif turn > 1:
            random = airandom(tiles)
            tiles[random[0]][random[1]] = playertosign(player)
            return True

def playertosign(player):
    if player == 0:
        return "O"
    return "X"

def showinterface():
    os.system("clear")
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
