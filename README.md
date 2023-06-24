# Maze Solver

This repository contains Python code that implements a maze-solving algorithm using Depth-First Search (DFS). The code takes an initial maze state and finds the path from a start state to a goal state.

## Maze Representation

The maze is represented as a 2-dimensional array, where each element represents a cell in the maze. The following conventions are used:

- `0`: Represents a wall or obstacle in the maze.
- `1`: Represents an open path or corridor in the maze.

The initial maze is defined in the `initial_State_maze` variable as a 2D array.

## Available Functions

The code provides several functions to facilitate maze solving:

### Check_Up(maze, currentState)

This function checks if there is an open path in the upward direction from the current state in the maze. It returns `True` if there is an open path and `False` otherwise.

### Check_Left(maze, currentState)

This function checks if there is an open path in the leftward direction from the current state in the maze. It returns `True` if there is an open path and `False` otherwise.

### Check_Right(maze, currentState)

This function checks if there is an open path in the rightward direction from the current state in the maze. It returns `True` if there is an open path and `False` otherwise.

### Check_Down(maze, currentState)

This function checks if there is an open path in the downward direction from the current state in the maze. It returns `True` if there is an open path and `False` otherwise.

### Node_dfs(direction, x, y)

This class represents a node in the Depth-First Search algorithm. It stores the direction, x-coordinate, and y-coordinate of a node.

### ValidateVisitedNodes(x, y, visitednodes)

This function checks if a node with the given x and y coordinates has been visited before. It returns `True` if the node has not been visited, and `False` otherwise.

### ValidateVisitedNodes_DFS(direction, x, y, visitednodes)

This function checks if a node with the given direction, x, and y coordinates has been visited before. It returns `True` if the node has not been visited, and `False` otherwise.

### create_node(state, x, y)

This function creates a new `Node_dfs` object with the given state, x-coordinate, and y-coordinate.

### dfs_Algo(maze, startState, goalState)

This function implements the Depth-First Search algorithm to find the path from the start state to the goal state in the maze. It returns the cost (number of steps) required to reach the goal state.

### bfs_Algo(maze, startState, goalState)

This function implements the Breadth-First Search algorithm to find the path from the start state to the goal state in the maze. It returns the cost (number of steps) required to reach the goal state.

## Usage

To use the maze solver algorithm, follow these steps:

1. Define the initial maze state by modifying the `initial_State_maze` variable.

2. Set the `start_State` and `goalState` variables to the desired start and goal states in the maze.

3. Run the script.

## Example

```python
# Define the initial maze state
initial_State_maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 

1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Set the start and goal states
start_State = [4, 11]
goalState = [10, 0]

# Solve the maze using Depth-First Search
cost_dfs = dfs_Algo(initial_State_maze, start_State, goalState)
print("The Total Cost Using DFS Is:", cost_dfs)
```

