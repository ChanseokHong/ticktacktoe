

def aexam(tiles):
    i = 0
    while i < 3:
        if (tiles[i][0] == "X") and (tiles[i][1] == "X") and (tiles[i][2] == "X"):
            return True
        elif (tiles[0][i] == "X") and (tiles[1][i] == "X") and (tiles[2][i] == "X"):
            return True
        i += 1
    if (tiles[0][0] == "X") and (tiles[1][1] == "X") and (tiles[2][2] == "X"):
        return True
    elif (tiles[2][0] == "X") and (tiles[1][1] == "X") and (tiles[0][2] == "X"):
        return True
    return False


def bexam(tiles):
    i = 0
    while i < 3:
        if (tiles[i][0] == "O") and (tiles[i][1] == "O") and (tiles[i][2] == "O"):
            return True
        elif (tiles[0][i] == "O") and (tiles[1][i] == "O") and (tiles[2][i] == "O"):
            return True
        i += 1
    if (tiles[0][0] == "O") and (tiles[1][1] == "O") and (tiles[2][2] == "O"):
        return True
    elif (tiles[2][0] == "O") and (tiles[1][1] == "O") and (tiles[0][2] == "O"):
        return True
    return False


def exam(tiles):
    if " " not in tiles[0] and " " not in tiles[1] and " " not in tiles[2]:
        return True
    return False
