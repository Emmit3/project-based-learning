import numpy as np
def random_state(width, height):
    state = dead_state(width, height)
    #for each val in state: 
        # for each row in val: 

def dead_state(width, height):
    board_state = np.zeros((width,height)) #check array access
    #np.zeros executes as zeros(shape); in this case the shape is the width and height 
    return board_state
width = 6; 
height = 5; 
print(dead_state(width, height))
