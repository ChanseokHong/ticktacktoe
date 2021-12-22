import random


def aiwin(tiles):
    i = 0
    while i < 3:
        n = 0
        k = 0
        if tiles[i][0] == "X":
            n += 1
        else:
            k = 0
        if tiles[i][1] == "X":
            n += 1
        else:
            k = 1
        if tiles[i][2] == "X":
            n += 1
        else:
            k = 2
        if n == 2:
            if tiles[i][k] == " ":
                return [i, k]
        i += 1
    while i < 3:
        n = 0
        k = 0
        if tiles[0][i] == "X":
            n += 1
        else:
            k = 0
        if tiles[1][i] == "X":
            n += 1
        else:
            k = 1
        if tiles[2][i] == "X":
            n += 1
        else:
            k = 2
        if n == 2:
            if tiles[k][i] == " ":
                return [k, i]
        i += 1

    n = 0
    k = 0
    if tiles[0][0] == "X":
        n += 1
    else:
        k = 0
    if tiles[1][1] == "X":
        n += 1
    else:
        k = 1
    if tiles[2][2] == "X":
        n += 1
    else:
        k = 2
    if n == 2:
        if tiles[k][k] == " ":
            return [k, k]
    n = 0
    k = 0
    if tiles[2][0] == "X":
        n += 1
    else:
        k = 0
    if tiles[1][1] == "X":
        n += 1
    else:
        k = 1
    if tiles[0][2] == "X":
        n += 1
    else:
        k = 2
    if n == 2:
        if tiles[2-k][k] == " ":
         return [2-k, k]


def ailose(tiles):
    i = 0
    while i < 3:
        n = 0
        k = 0
        if tiles[i][0] == "O":
            n += 1
        else:
            k = 0
        if tiles[i][1] == "O":
            n += 1
        else:
            k = 1
        if tiles[i][2] == "O":
            n += 1
        else:
            k = 2
        if n == 2:
            if tiles[i][k] == " ":
                return [i, k]
        i += 1
    while i < 3:
        n = 0
        k = 0
        if tiles[0][i] == "O":
            n += 1
        else:
            k = 0
        if tiles[1][i] == "O":
            n += 1
        else:
            k = 1
        if tiles[2][i] == "O":
            n += 1
        else:
            k = 2
        if n == 2:
            if tiles[k][i] == " ":
                return [k, i]
        i += 1
    n = 0
    k = 0
    if tiles[0][0] == "O":
        n += 1
    else:
        k = 0
    if tiles[1][1] == "O":
        n += 1
    else:
        k = 1
    if tiles[2][2] == "O":
        n += 1
    else:
        k = 2
    if n == 2:
        if tiles[k][k] == " ":
            return [k, k]
    n = 0
    k = 0
    if tiles[2][0] == "O":
        n += 1
    else:
        k = 0
    if tiles[1][1] == "O":
        n += 1
    else:
        k = 1
    if tiles[0][2] == "O":
        n += 1
    else:
        k = 2
    if n == 2:
        if tiles[2-k][k] == " ":
            return [2-k, k]


def airandom(tiles):
    var = [0, 1, 2]
    x = random.choice(var)
    y = random.choice(var)
    while not tiles[x][y] == " ":
        x = random.choice(var)
        y = random.choice(var)
    return [x,y]
