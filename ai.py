import random


def basicai(tiles,player):
    if player == 0:
        try:
            return checkwin(tiles,"X")
        except:
            return checkwin(tiles,"O")
    else:
        try:
            return checkwin(tiles,"O")
        except:
            return checkwin(tiles,"X")

def checkwin(tiles,symbol):
    i = 0;n = 0;m = 0;j = 0;a = 0;b = 0;c1 = 0;c2 = 0;c3 = 0;c4 = 0
    while i < 3:
        while j < 3:
            if tiles[i][j] == symbol:
                n += 1
            else:
                c1 = j
            if tiles[j][i] == symbol:
                m += 1
            else:
                c2 = j
            j += 1
        if n == 2:
            if tiles[i][c1] == " ":
                return [i,c1]
        if m == 2:
            if tiles[c2][i] == " ":
                return [c2,i]
        if tile[i][i] == symbol:
            a += 1
        else:
            c3 = i
        if tile[2-i][i] == symbol:
            b += 1
        else:
            c4 = i
        i += 1
        if a == 2:
            return [c3,c3]
        if b == 2:
            return [2-c4,c4]


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
