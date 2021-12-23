import random


def basicai(tiles,player):
    x = checkwin(tiles,"X")
    o = checkwin(tiles,"O")
    if player == 0:
        if o is not None:
            return o
        else:
            return x
    else:
        if x is not None:
            return x
        else:
            return o

def checkwin(tiles,symbol):
    h = horcheck(tiles,symbol)
    if h is not None:
        return h
    v = vercheck(tiles,symbol)
    if v is not None:
        return v
    c = crosscheck(tiles,symbol)
    if c is not None:
        return c


def horcheck(tiles,symbol):
    i = 0
    while i < 3:
        n = 0;a = -1
        if tiles[i][0] == symbol:
            n += 1
        else:
            a = 0
        if tiles[i][1] == symbol:
            n += 1
        else:
            a = 1
        if tiles[i][2] == symbol:
            n += 1
        else:
            a = 2
        if n == 2:
            if not a == -1:
                if tiles[i][a] == " ":
                    return [i,a]
        i += 1

def vercheck(tiles,symbol):
    i = 0
    while i < 3:
        n = 0;a = -1
        if tiles[0][i] == symbol:
            n += 1
        else:
            a = 0
        if tiles[1][i] == symbol:
            n += 1
        else:
            a = 1
        if tiles[2][i] == symbol:
            n += 1
        else:
            a = 2
        if n == 2:
            if not a == -1:
                if tiles[a][i] == " ":
                    return [a,i]
        i += 1


def crosscheck(tiles,symbol):
    i=0;a=0;b=0
    while i < 3:
        if tiles[i][i] == symbol:
            a += 1
        else:
            c = i
        if tiles[2-i][i] == symbol:
            b += 1
        else:
            d = i
        i += 1
    if a == 2:
        if tiles[c][c] == " ":
            return [c,c]
    if b == 2:
        if tiles[2-d][d] == " ":
            return [2-d,d]


def airandom(tiles):
    var = [0, 1, 2]
    x = random.choice(var)
    y = random.choice(var)
    while not tiles[x][y] == " ":
        x = random.choice(var)
        y = random.choice(var)
    return [x,y]

def aihardstart(tiles):
    var = [[0,0],[2,2],[0,2],[2,0]]
    output = random.choice(var)
    return output

def aihardsec(tiles):
    corner = [[0,0],[2,2],[0,2],[2,0]]
    i = 0
    while i < 4:
        if tiles[corner[i,0],corner[i,1]] == "X":
            return random.choice(var)
        i += 1
    if tiles[2][2] == "X":
        var = [[0,0],[0,2],[2,0],[2,2]]
        return random.choice(var)
