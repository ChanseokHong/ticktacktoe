# import pygame
from game import game


def main():
    # error = False
    # error = startgame()
    # if(error == True):
    #     print("unexpected input")

    game()


# def start():
#     print("playing with ai y/n")
#     gamemode = input()
#     if gamemode == "y" or gamemode == "Y":
#         return startgame(0)
#     elif gamemode == "n" or gamemode == "N":
#         return startgame(1)
#     else:
#         return False


# def startgame(islocal):
#     if islocal == True:
#         game(0)
    # elif islocal == False:
    #     print("choose dificulty 1-3")
    #     ai_dif = input()
    #     if ai_dif in aidif_lis:
    #         game(ai_dif)
    # else:
    # return True


if __name__ == "__main__":
    main()
