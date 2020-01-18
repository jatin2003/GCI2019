# 20 Queen

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# import modules
from random import randint
import sys

# 
no = 20
chess = []

for a in range(no):
    row = [2] * no
    chess.append(row)
mess = []

for a in range(no**2):
    mess.append([])

def fill(i, j):
    global chess, mess
    chess[i][j] = 'Q'
    for a in range(no-1):
        chess[i - a - 1][j] = '-'
        mess[(i - a - 1) * no + j].append(i * no + j + 1)
        chess[i][j - a - 1] = '-'
        if (i + 1) * no - a - 1 > i * no + j:
            mess[(i + 1) * no - a - 1].append(i * no + j + 1)
        else:
            mess[(i + 1) * no - a - 2].append(i * no + j + 1)
        if i - a - 1 >= 0 and j - a - 1 >= 0:
            chess[i - a - 1][j - a - 1] = '-'
            mess[(i - a - 1) * no + j - a - 1].append(i * no + j + 1)
        if i - a - 1 >= 0 and j + a + 1 <= (no-1):
            chess[i - a - 1][j + a + 1] = '-'
            mess[(i - a - 1) * no + j + a + 1].append(i * no + j + 1)
        if i + a + 1 <= (no-1) and j - a - 1 >= 0:
            chess[i + a + 1][j - a - 1] = '-'
            mess[(i + a + 1) * no + j - a - 1].append(i * no + j + 1)
        if i + a + 1 <= (no-1) and j + a + 1 <= (no-1):
            chess[i + a + 1][j + a + 1] = '-'
            mess[(i + a + 1) * no + j + a + 1].append(i * no + j + 1)


def unfill(i, j):
    global chess, mess
    chess[i][j] = 2
    arg = i * no + j + 1
    for a in range(no**2):
        if arg in mess[a]:
            while arg in mess[a]:
                mess[a].remove(arg)
            if not any(mess[a]):
                p = a // no
                q = a % no
                chess[p][q] = 2


space = []
for a in range(no):
    Toss = randint(0,no-1)
    while Toss in space:
        Toss = randint(0,no-1)
    space.append(Toss)


x = 0
def Queen():
    global chess, mess, x
    for a in range(no):
        if chess[space[x]][a] == 2:
            fill(space[x], a)
            x += 1
            if x < no:
                Queen()
                x -= 1
                for b in range(no):
                    if chess[space[x]][b] == 'Q':
                        unfill(space[x], b)
            else:
                for v in range(no):
                    print(' '.join(chess[v]))
                sys.exit()
        else:
            if a == no- 1:
                for b in range(no):
                    if chess[space[x - 1]][b] == 1:
                        unfill(space[x - 1], b)
                        break

Queen()
