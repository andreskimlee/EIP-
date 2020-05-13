# Traversing a graph/ reconstructing a graph given a single node:

# iterative DFS solution.


# The approach is simple. Use a dictionairy/set to keep track of visted notes. use a queue or stack to keep track of nodes to visit.


# from collections import deque


# def cloneGraph2(self, node):
#     if not node:  # edge case in case node is empty.
#         return
#     # Create a instance of the first node given/
#     nodeCopy = UndirectedGraphNode(node.label)
#     # create a dictionairy with node pointing to node object.
#     dic = {node: nodeCopy}
#     stack = [node]  # create a stack with oen node.
#     while stack:  # iterate until stack is empty.
#         node = stack.pop()  # remove from stack.
#         for neighbor in node.neighbors:  # iterate over that node's neighbors.
#             if neighbor not in dic:  # if the elemet in the node neighbors is not in dic
#                 # instantialize that node.
#                 neighborCopy = UndirectedGraphNode(neighbor.label)
#                 dic[neighbor] = neighborCopy  # put it in the dictionairy
#                 # key into our node and neighbors key which should be an empty array and append that node
#                 dic[node].neighbors.append(neighborCopy)
#                 # Append to the stack the newly discovered node.
#                 stack.append(neighbor)
#             else:  # else it means that the node is already there and has been visited.
#                 # mark the node just as a neighbor.
#                 dic[node].neighbors.append(dic[neighbor])
#     return nodeCopy


# Given a 2D array of black and white entries representing amaze with designated entrance and exit
# points, find a path from the entrance to the exit, if one exists 1 represents a wall 0 represents open space.
# ex input :
# [[1,0,0,0,0,0,1,1,0,E] node(1) : [0, 0]
#  [0,1,0,0,0,0,0,0,0,0]
#  [1,1,0,0,1,1,0,0,1,1]
#  [0,0,1,1,1,0,0,0,1,0]
#  [0,1,1,0,0,0,0,0,0,0]
#  [0,1,1,0,0,1,0,1,1,0]
#  [0,0,0,0,1,0,0,0,0,0]
#  [1,0,1,0,1,0,1,0,0,0]
#  [1,0,1,1,0,0,0,1,1,1]
#  [S,0,0,0,0,0,0,1,1,0]]


# Focus on the inverse cases only where you just find the whites on the edges. Then set it equal to a placeholder  = "T"
# if on edge and white board[x][y] = "T"

# iterate over the board again and convert all whites to black. and if T return to white.
# when x = 0 and y = 0 and y = 3 and x = 4
# [W ,B  B]
# [W ,W  B]
# [W ,B  B]
# [B ,B  B] < -- [2,3]


from collections import deque


def ComputeEnclosedRegions(board):
    queueStack = deque()
    for x in range(0, len(board)):
        for y in range(0, len(board[1])):
            if x == 0 or y == 0 or x == (len(board[1]) - 1) or y == (len(board) - 1):
                queueStack.append([x, y])

    while queueStack:
        coordin = queueStack.pop()

        x, y = coordin[0], coordin[1]
        if board[x][y] == "W":
            print(x, y)
            board[x][y] = "T"
            queueStack.extend(([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]))

    for x in range(0, len(board)):
        for y in range(0, len(board[1])):
            board[x][y] = "B" if board[x][y] != "T" else "W"

    return board


arr = [["W", "B",  "B"],
       ["B", "W",  "B"],
       ["W", "B",  "B"],
       ["B", "B",  "B"]]

print(ComputeEnclosedRegions(arr))
