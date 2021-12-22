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
            return (str(i), str(k))
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
            return (str(k), str(i))
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
        return (str(k), str(k))
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
        return (str(2-k), str(k))
    return False


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
            return (str(i), str(k))
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
            return (str(k), str(i))
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
        return (str(k), str(k))
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
        return (str(2-k), str(k))


def airandom(tiles):
    var = [0, 1, 2]
    x = ""
    y = ""
    while tiles[x][y] == "":
        x = random.choice(var)
        y = random.choice(var)
    return (str(x), str(y))
