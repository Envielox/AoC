with open('5.in') as f:
    a = [x[:-1] for x in f.readlines()]

numbers = [int(x) for x in a[0].split(",")]
boards = []

for i in range(1, len(a), 6):
    z = a[i+1:i+6]
    b = [ [int(x) for x in row.split()] for row in z]
    boards.append(b)

def print_board(b):
    for r in b:
        for e in r:
            print('{:>2} '.format(e), end = '')
        print()

def is_winning_row(b):
    for y in range(5):
        wins = True
        for x in range(5):
            if b[y][x] != -1:
                wins = False
                break
        if wins:
            return True
    return False

def is_winning_col(b):
    for x in range(5):
        wins = True
        for y in range(5):
            if b[y][x] != -1:
                wins = False
                break
        if wins:
            return True
    return False

def play_board(b): # returns turn on which the board wins
    for i, n in enumerate(numbers):
        #print("playing {}".format(n))
        for y in range(5):
            for x in range(5):
                if b[y][x] == n:
                    b[y][x] = -1
        if is_winning_row(b) or is_winning_col(b):
            return i

def score_board(b):
    S = 0
    for y in range(5):
        for x in range(5):
            if b[y][x] != -1:
                S += b[y][x]
    return S
