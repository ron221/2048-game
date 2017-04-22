#
# CS1010S --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    return [[0,]*n]*n

def has_zero(mat):
    lst = flatten(mat)
    if lst.count(0):
        return True
    else:
        return False

def add_two(mat):
    a=randint(0,len(mat)-1)
    b=randint(0,len(mat)-1)
    while(mat[a][b]!=0):
        a=randint(0,len(mat)-1)
        b=randint(0,len(mat)-1)
    mat[a][b]=2
    return mat
k = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(add_two(k))
###########
# Task 2  #
###########

def game_status(mat):
    if 2048 in flatten(mat):
        return 'win'
    for i in range(len(mat)): #zero
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                return 'not over'
    for i in range(len(mat)-1): 
        for j in range(len(mat[0])-1):
            if mat[i][j]==mat[i+1][j] or mat[i][j+1]==mat[i][j]:
                return 'not over'
    for j in range(len(mat)-1): #last row
        if mat[len(mat)-1][j]==mat[len(mat)-1][j+1]:
            return 'not over'
    for j in range(len(mat)-1): #last column
        if mat[j][len(mat)-1]==mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'


##m1 =[[2, 4, 16, 4], [4, 2, 2, 2], [2, 4, 2, 4], [4, 2, 4, 8]]
m2 = [[4,2,4],[2,4,2],[4,2,4]]
##print(game_status(m1))
##print(game_status(m2))



###########
# Task 3a #
###########

def transpose(mat):
    s = []
    row = len(mat)
    col = len(mat[0])
    for y in range(col):
        t = []
        for x in range(row):
            t.append(mat[x][y])
        s.append(t)
    return s


###########
# Task 3b #
###########

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[i][len(mat)-j-1])
    return new

def reverse(mat):
    new=[]
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new

#print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
############
# Task 3ci #
############
def goleft(mat):
    new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    merged=False
    for i in range(0,len(mat)):
        k=0
        for j in range(0,len(mat)):
            if mat[i][j]!=0:
                new[i][k] = mat[i][j]
                if j!=k:
                    merged=True
                k+=1
    return (new,merged)
              
def merge(mat):
    merged=False
    score=0
    for i in range(len(mat)):
         for j in range(len(mat)-1):
             if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                 mat[i][j]*=2
                 mat[i][j+1]=0
                 score += (mat[i][j])
                 merged=True
    return (mat,merged,score)

    

def merge_up(mat):
    mat=transpose(mat)
    mat,merged=goleft(mat)
    r=merge(mat)
    score = r[2]
    mat=r[0]
    merged=merged or r[1]
    mat=goleft(mat)[0]
    mat=transpose(mat)
    return (mat,merged,score)

def merge_down(mat):
    mat=reverse(transpose(mat))
    mat,merged=goleft(mat)
    r=merge(mat)
    score = r[2]
    mat=r[0]
    merged=merged or r[1]
    mat=goleft(mat)[0]
    mat=transpose(reverse(mat))
    return (mat,merged,score)

def merge_left(mat):
    mat,merged = goleft(mat)
    r = merge(mat)
    score = r[2]
    mat = r[0]
    merged=merged or r[1]
    mat=goleft(mat)[0]
    return (mat,merged,score)

def merge_right(mat):
    mat=reverse(mat)
    mat,merged=goleft(mat)
    r=merge(mat)
    score = r[2]
    mat=r[0]
    merged=merged or r[1]
    mat=goleft(mat)[0]
    mat=reverse(mat)
    return (mat,merged,score)

m4 = [[2,0,0,0],[4,0,2,0],[2,0,0,0],[2,0,0,0]]
##print(merge_left(m4))
##print(merge_right(m4))
##print(merge_up(m4))
##print(merge_down(m4))
#==> ([[4, 0, 0, 0], [4, 2, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0]], True, 8)

##m5 = [[2,2,0,4],[4,4,2,0],[2,0,2,0],[2,4,4,0]]
##print(merge_left(m5))
##print(merge_right(m5))
##print(merge_up(m5))
##print(merge_down(m5))
#==> ([[4, 4, 0, 0], [8, 2, 0, 0], [4, 0, 0, 0], [2, 8, 0, 0]], True, 24)

m6 = [[2,2,2,2],[4,0,2,0],[2,0,2,0],[2,0,0,0]]
#print(merge_left(m6))
#==> ([[4, 4, 0, 0], [4, 2, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0]], True, 12)

#############
# Task 3cii #
#############




###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return [matrix,total_score]

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    matrix =  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    add_two(matrix)
    add_two(matrix)
    return make_state(matrix,0)


def left(state):
    result = merge_left(get_matrix(state))
    print(result)
    if result[1] == False:
        add_two(result[0])
    else:
        state[0] = result[0]
        state[1] += result[2]
    return ([state[0],state[1]],result[1])


def right(state):
    result = merge_right(get_matrix(state))
    print(result)
    if result[1] == False:
        add_two(result[0])
    else:
        state[0] = result[0]
        state[1] += result[2]
    return ([state[0],state[1]],result[1])
    
def up(state):
    result = merge_up(get_matrix(state))
    print(result)
    if result[1] == False:
        add_two(result[0])
    else:
        state[0] = result[0]
        state[1] += result[2]
    return ([state[0],state[1]],result[1])

def down(state):
    result = merge_down(get_matrix(state))
    print(result)
    if result[1] == False:
        add_two(result[0])
    else:
        state[0] = result[0]
        state[1] += result[2]
    return ([state[0],state[1]],result[1])

# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)


#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    "Your answer here"

def get_record_matrix(record):
    "Your answer here"

def get_record_increment(record):
    "Your answer here"

############
# Task 5ii #
############

def make_new_records():
    "Your answer here"

def push_record(new_record, stack_of_records):
    "Your answer here"

def is_empty(stack_of_records):
    "Your answer here"

def pop_record(stack_of_records):
    "Your answer here"

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"

def get_matrix(state):
    "Your answer here"

def get_score(state):
    "Your answer here"

def make_new_game(n):
    "Your answer here"

def left(state):
    "Your answer here"

def right(state):
    "Your answer here"

def up(state):
    "Your answer here"

def down(state):
    "Your answer here"

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"

def undo(state):
    "Your answer here"


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
#gamegrid = GameGrid(game_logic)
