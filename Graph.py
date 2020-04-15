# Traversing a graph/ reconstructing a graph given a single node:

# iterative DFS solution.


def cloneGraph2(self, node):
    if not node:  # edge case in case node is empty.
        return
    # Create a instance of the first node given/
    nodeCopy = UndirectedGraphNode(node.label)
    # create a dictionairy with node pointing to node object.
    dic = {node: nodeCopy}
    stack = [node]  # create a stack with oen node.
    while stack:  # iterate until stack is empty.
        node = stack.pop()  # remove from stack.
        for neighbor in node.neighbors:  # iterate over that node's neighbors.
            if neighbor not in dic:  # if the elemet in the node neighbors is not in dic
                # instantialize that node.
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy  # put it in the dictionairy
                # key into our node and neighbors key which should be an empty array and append that node
                dic[node].neighbors.append(neighborCopy)
                # Append to the stack the newly discovered node.
                stack.append(neighbor)
            else:  # else it means that the node is already there and has been visited.
                # mark the node just as a neighbor.
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy


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

def traverseGraph(maze):
    for i in range(len(maze)):
        for j in range((i, len(maze)):
