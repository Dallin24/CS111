from Grid import Grid
from copy import deepcopy
import random


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    rock = 'r'
    grid_copy = deepcopy(grid)
    
    for y in range(grid_copy.height):
        for x in range(grid_copy.width):
            if(grid_copy.get(x, y) == None):
                if (random.random() <= chance_of_rock):
                    grid_copy.set(x,y,rock)
                    
    return grid_copy


def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    
    bubble = 'b'
    grid_copy = deepcopy(grid)
    
    for y in range(grid_copy.height):
        for x in range(grid_copy.width):
            if(grid_copy.get(x, y) == None):
                if (random.random() <= chance_of_bubbles):
                    grid_copy.set(x,y,bubble)
                    
    return grid_copy


def modify_grid(grid, func, prob):
    """Write a function which can take in a grid, a function
    and a probablily as parameters and updates the grid using
    the function passed in."""
    "*** YOUR CODE HERE ***"
    
    for y in range(grid.height):
        for x in range(grid.width):
            if(grid.get(x, y) == None):
                if (random.random() <= prob):
                    func(x,y)


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    "*** YOUR CODE HERE ***"
    bubble = 'b'
    grid_copy = deepcopy(grid)
    
    if grid_copy.get(x,y) == bubble: grid_copy.set(x,y,None)        
    if(y >= 0): grid_copy.set(x,(y-1),bubble)
    
    return grid_copy


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    bubble = 'b'
    grid_copy = deepcopy(grid)
    
    for y in range(grid_copy.height):
        for x in range(grid_copy.width):
            if(grid_copy.get(x,y) == bubble) and (y > 0) and (grid_copy.get(x,(y-1)) == None):
                grid_copy.set(x,y,None)
                grid_copy.set(x,(y-1),bubble)
    
    return grid_copy
    

def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1
