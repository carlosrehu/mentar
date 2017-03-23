"""Project 3 - Motion Planning
Uses the Manhattan distance and A* Search to calculate the 
shortest past from start to finish with randomly generated obstacles"""

#Imports
from random import random
from random import seed
from Queue import PriorityQueue
from copy import deepcopy


class State(object):
    
    def __init__(self, start_position, goal_position, start_grid):
        """ Initializes current position, goal position, grid, and total
            number of moves made """
        self.position = start_position
        self.goal = goal_position
        self.grid = start_grid
        self.total_moves = 0
        
    #--- Fill in the rest of the class...
    
    def manhattan_distance(self):
        """ Calculates and returns the heuristic distance from start to goal"""
        distance = abs(self.position[0]-(num_rows-2)) + abs(self.position[1]-(num_cols-2))
    
        return distance;
        
        
    def finished(self):
        """ If the current position matches the goal position, return True for complete"""
        if self.position != self.goal:
            return False
        print 'Solution'
        return True
        
        
    def move(self, direction, visited, x, y):
        """Determines coordinates based on given direction
        Marks the current working position with a star to indicate path
        Creates a new state from the move if no obstacles are present"""
        
        # Determine x and y coordinates for new position from direction
        if direction == 'up':
            new_x = x-1
            new_y = y
            
        if direction == 'down':
            new_x = x+1
            new_y = y
                    
        if direction == 'left':
            new_x = x
            new_y = y-1
                
        if direction == 'right':
            new_x = x
            new_y = y+1
            
        # Generate a new state from the move if it's possible
        if self.grid[new_x][new_y] != 1:
            
            new_pos = (new_x, new_y)
            goal_pos = (num_rows-2, num_cols-2)
            
            new_grid = deepcopy(self.grid)
            # Mark the path with a * 
            new_grid[new_x][new_y] = '*'
            
            new_state = State(new_pos, goal_pos, new_grid)
            new_state.total_moves = self.total_moves + 1
                
            return new_state
            
        # If the swap was not possible, return None
        else:
            return None
        

def create_grid():
    
    """Create and return a randomized grid
    
        0's in the grid indcate free squares
        1's indicate obstacles
        
        DON'T MODIFY THIS ROUTINE.
    """
    
    # Start with a num_rows by num_cols grid of all zeros
    grid = [[0 for c in range(num_cols)] for r in range(num_rows)]
    
    # Put ones around the boundary
    grid[0] = [1 for c in range(num_cols)]
    grid[num_rows - 1] = [1 for c in range(num_cols)]

    for r in range(num_rows):
        grid[r][0] = 1
        grid[r][num_cols - 1] = 1
            
    # Sprinkle in obstacles randomly
    for r in range(1, num_rows - 1):
        for c in range(2, num_cols - 2):
            if random() < obstacle_prob:
                grid[r][c] = 1;

    # Make sure the goal and start spaces are clear
    grid[1][1] = 0
    grid[num_rows - 2][num_cols - 2] = 0
            
    return grid
    

    

def print_grid(grid):
    
    """Print a grid, putting spaces in place of zeros for readability
    
       DON'T MODIFY THIS ROUTINE.
    """
    
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                print ' ',  # Ending comma prevents automatic newline
            else:
                print grid[r][c],
        print ''
            
    print ''

    return 


def main():
    """ Initialize grids and positions
    Processes the best path using A* search """
    
    # Setup the randomized grid
    grid = create_grid()
    print_grid(grid)
    
    # Initialize the starting state and priority queue
    start_position = (1, 1)
    goal_position = (num_rows - 2, num_cols - 2)
    start_state = State(start_position, goal_position, grid)
    start_state.grid[1][1] = '*'
    priority = start_state.total_moves + start_state.manhattan_distance()
    
    queue = PriorityQueue()

    queue.put((priority, start_state))
    
    # Initialize dictionary to record previously visited
    visited = {}
    
    while queue.qsize() > 0:
        
        # Pop the state 
        queue_item = queue.get()
        state = queue_item[1]
        visited[state.position] = True
        
        # Check if this state corresponds with finishing condition
        if state.finished():
            print_grid(state.grid)
            return

        for direction in ['up', 'down', 'left', 'right']:
            # Attempts to move in given direction
            x = state.position[0]
            y = state.position[1]
            new_state = state.move(direction, visited, x, y)
            if new_state is None:
                continue
            
            # If the state has not been visited, add it to the queue
            if new_state.position not in visited:

                # Insert into the priority queue
                queue.put((new_state.total_moves + new_state.manhattan_distance(), new_state))
    
    print 'No solution found'

if __name__ == '__main__':
    
    seed(0)
    
    #--- Easy mode
    
    # Global variables --- saves us the trouble of continually passing them as
    # parameters to every routine
    num_rows = 8
    num_cols = 16
    obstacle_prob = .20
    
    for trial in range(5):
        print '\n\n-----Easy trial ' + str(trial + 1) + '-----'
        main()
        
    #--- Uncomment the following sets of trials when you're ready
        
    #--- Hard mode
    num_rows = 15
    num_cols = 30
    obstacle_prob = .30
    
    for trial in range(5):
        print '\n\n-----Harder trial ' + str(trial + 1) + '-----'
        main()
        
    #--- INSANE mode
    num_rows = 20
    num_cols = 60
    obstacle_prob = .35
    
    for trial in range(5):
        print '\n\n-----INSANE trial ' + str(trial + 1) + '-----'
        main()