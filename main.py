initial_State_maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
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


def Check_Up(maze, currentState):
    if currentState[0] != 0:
        if maze[currentState[0] - 1][currentState[1]] != 0:
            return True
        else:
            return False
    else:
        return False


def Check_left(maze, currentState):
    if currentState[1] != 0:
        if maze[currentState[0]][currentState[1] - 1] != 0:
            return True
        else:
            return False
    else:
        return False


def Check_Right(maze, currentState):
    sizeofmaze = len(maze[0])
    if currentState[1] != sizeofmaze - 1:
        if maze[currentState[0]][currentState[1] + 1] != 0:
            return True
        else:
            return False
    else:
        return False


def Check_Down(maze, currentState):
    sizeofmaze = len(maze[0])

    if currentState[1] != sizeofmaze - 1:
        if maze[currentState[0] + 1][currentState[1]] != 0:
            return True
        else:
            return False
    else:
        return False


class Node_dfs:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y


def ValidateVisitedNodes(x, y, visitednodes):
    for objs in visitednodes:
        if x == objs.x:
            if y == objs.y:
                return False
    return True


def ValidateVisitedNodes_DFS(direction, x, y, visitednodes):
    for objs in visitednodes:
        if direction == objs.direction:
            if x == objs.x:
                if y == objs.y:
                    return False
    return True


def create_node(state, x, y):
    return Node_dfs(state, x, y)


def bfs_Algo(maze, startState, goalState):
    cost = 0
    queue = []
    visitednotes = []
    queue.append(create_node("none", startState[0], startState[1]))
    number = 0
    while True:
        currentState = queue.pop(0)
        print("QUEUE POPEDD", currentState.direction, currentState.x, currentState.y)
        if (Check_Up(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes(currentState.x - 1, currentState.y, visitednotes)
        ):
            queue.append(create_node("up", currentState.x - 1, currentState.y))

        if (Check_left(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes(currentState.x, currentState.y - 1, visitednotes)
        ):
            queue.append(create_node("left", currentState.x, currentState.y - 1))

        if (Check_Right(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes(currentState.x, currentState.y + 1, visitednotes)
        ):
            queue.append(create_node("right", currentState.x, currentState.y + 1))

        if (Check_Down(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes(currentState.x + 1, currentState.y, visitednotes)
        ):
            queue.append(create_node("down", currentState.x + 1, currentState.y))

        visitednotes.append(create_node("none", currentState.x, currentState.y))
        for objs in visitednotes:
            if (objs.x == goalState[0]) & (objs.y == goalState[1]):
                return number

        print("///////////////////////////number :", number)

        print("QUEUEUEEEE")
        for temp in queue:
            print("queue ", temp.direction, temp.x, temp.y)

        number += 1


def dfs_Algo(maze, startState, goalState):
    cost = 0
    stack = []
    visitednotes = []
    stack.append(create_node("none", startState[0], startState[1]))

    while True:
        currentState = stack.pop()
        print("stack POPED", currentState.direction, currentState.x, currentState.y)

        if (Check_Up(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes_DFS(
                "up", currentState.x - 1, currentState.y, visitednotes
            )
        ):
            stack.append(create_node("up", currentState.x - 1, currentState.y))

        if (Check_Right(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes_DFS(
                "right", currentState.x, currentState.y + 1, visitednotes
            )
        ):
            stack.append(create_node("right", currentState.x, currentState.y + 1))

        if (Check_left(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes_DFS(
                "left", currentState.x, currentState.y - 1, visitednotes
            )
        ):
            stack.append(create_node("left", currentState.x, currentState.y - 1))

        if (Check_Down(maze, [currentState.x, currentState.y])) & (
            ValidateVisitedNodes_DFS(
                "down", currentState.x + 1, currentState.y, visitednotes
            )
        ):
            stack.append(create_node("down", currentState.x + 1, currentState.y))

        visitednotes.append(
            create_node(currentState.direction, currentState.x, currentState.y)
        )

        print(
            "Stack's nodes ....//////////////////////////////////////////////////////////"
        )
        for objs in stack:
            print("node ", objs.x, objs.y, objs.direction)
        print(
            "visited nodes ....//////////////////////////////////////////////////////////"
        )
        for objs in stack:
            print("node ", objs.x, objs.y, objs.direction)
            if (objs.x == goalState[0]) & (objs.y == goalState[1]):
                return cost

        cost += 1
        print("cost now: ", cost)
        print(
            "////////////////////iteration end///////////////////////////////////////////////////////////////////////"
        )


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print(
        "///////////////////////////// DFS ALGO ///////////////////////////////////////////////"
    )
    start_State = [4, 11]
    goalState = [10, 0]
    print("Start State :", start_State)
    print("Goal State : ", goalState)

    cost_dfs = dfs_Algo(initial_State_maze, start_State, goalState)
    print("The Total Cost Using Dfs Is : ", cost_dfs)
