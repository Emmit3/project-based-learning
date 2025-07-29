import numpy as np
import sys
import os
import time
# 1: storing the board state 
def random_state(width, height):
    state = dead_state(width, height) # random array (width, height) of 0s 
    for row in state: #rows 
        for idx, _ in enumerate(row): #column parsing
            randomValue = np.random.random() 
            if(randomValue >= 0.5):
                row[idx] = 1
            else:
                row[idx] = 0
    return state
def dead_state(width, height):
    board_state = np.zeros((height,width)) #check array access
    #np.zeros executes as zeros(shape); in this case the shape is the width and height 
    return board_state
# 2: pretty printing 
def render(board_state):
    for row in board_state:
        for num in row:
            if(num == 1):
                print('\u25a0' + ' ', end = '') # "black square" (white in terminal)
            else: 
                print('\u25a1' + ' ', end = '') # "white square" (black in terminal) 
        print('') #next line
# 3: calculating next state
def next_board_state(initial_board):
    height = len(initial_board)
    width = len(initial_board[0])
    new_state = dead_state(width, height)
    for rowIdx, row in enumerate(initial_board):
        for idx, val in enumerate(row):
            if idx == 0: #corner case for left edge
                if rowIdx == 0: # top left case
                    sum = (initial_board[rowIdx][idx + 1] + initial_board[rowIdx + 1][idx + 1] + initial_board[rowIdx + 1][idx])
                    if val == 0: # dead top left 
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else: # alive top left 
                        if(sum >= 2):
                            new_state[rowIdx][idx] = 1 #keeps one if there are at least two neighbors 
                elif rowIdx == height - 1: # bottom left case
                    sum = (initial_board[rowIdx][idx + 1] + initial_board[rowIdx - 1][idx + 1] + initial_board[rowIdx - 1][idx])
                    if val == 0: # dead bot left 
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else: # alive bot left 
                        if(sum >= 2):
                            new_state[rowIdx][idx] = 1
                # Left edge 
                else:
                    sum = (initial_board[rowIdx][idx + 1] + initial_board[rowIdx - 1][idx + 1] + initial_board[rowIdx - 1][idx]
                           + initial_board[rowIdx + 1][idx + 1] + initial_board[rowIdx + 1][idx])
                    if val == 0: 
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else: 
                        if(sum == 2 or sum == 3):
                            new_state[rowIdx][idx] = 1
            elif idx == width - 1: #corner case for right edge 
                if rowIdx == 0: # top right case
                    sum = (initial_board[rowIdx][idx - 1] + initial_board[rowIdx + 1][idx - 1] + initial_board[rowIdx + 1][idx])
                    if val == 0: # dead top right
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else: # alive top right 
                        if(sum >= 2):
                            new_state[rowIdx][idx] = 1
                elif rowIdx == height - 1: # bottom right case
                    sum = (initial_board[rowIdx][idx - 1] + initial_board[rowIdx - 1][idx - 1] + initial_board[rowIdx - 1][idx])
                    if val == 0: # dead bot right
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else: # alive bot right 
                        if(sum >= 2):
                            new_state[rowIdx][idx] = 1
                #Right edge 
                else:
                    sum = (initial_board[rowIdx][idx - 1] + initial_board[rowIdx - 1][idx - 1] + initial_board[rowIdx - 1][idx] +
                            initial_board[rowIdx + 1][idx - 1] + initial_board[rowIdx + 1][idx])
                    if val == 0:
                        if(sum == 3):
                            new_state[rowIdx][idx] = 1
                    else:
                        if(sum == 2 or sum == 3): 
                            new_state[rowIdx][idx] = 1
            elif rowIdx == 0: #top edge case
                sum = (initial_board[rowIdx][idx - 1] + initial_board[rowIdx][idx + 1] + initial_board[rowIdx + 1][idx]
                       + initial_board[rowIdx + 1][idx - 1] + initial_board[rowIdx + 1][idx + 1])
                if val == 0:
                    if(sum == 3):
                        new_state[rowIdx][idx] = 1
                else:
                    if(sum == 2 or sum == 3): 
                        new_state[rowIdx][idx] = 1
            elif rowIdx == height - 1: #bottom edge case
                sum = (initial_board[rowIdx][idx - 1] + initial_board[rowIdx][idx + 1] + initial_board[rowIdx - 1][idx]
                    + initial_board[rowIdx - 1][idx - 1] + initial_board[rowIdx - 1][idx + 1])
                if val == 0:
                    if(sum == 3):
                        new_state[rowIdx][idx] = 1
                else:
                    if(sum == 2 or sum == 3): 
                        new_state[rowIdx][idx] = 1
            else:
                sum = (initial_board[rowIdx][idx + 1] + initial_board[rowIdx][idx - 1] + initial_board[rowIdx + 1][idx] + initial_board[rowIdx - 1][idx] +
                    initial_board[rowIdx + 1][idx + 1] + initial_board[rowIdx + 1][idx - 1] + initial_board[rowIdx - 1][idx + 1] + initial_board[rowIdx - 1][idx - 1])
                if val == 0:
                    if(sum == 3):
                        new_state[rowIdx][idx] = 1
                else:
                    if(sum == 2 or sum == 3): 
                        new_state[rowIdx][idx] = 1
    return new_state 
def clearTerminal():
    _ = os.system('cls')
def main(): 
    sys.stdout.reconfigure(encoding='utf-8')  # changing character output 
    width = int(input('Please enter a width: ')) 
    height = int(input('Please enter a height: ')) 
    board = random_state(width, height)
    while(True):
        render(board)
        time.sleep(0.2)
        board = next_board_state(board)
        clearTerminal() 
if __name__ == '__main__': 
    main() 


