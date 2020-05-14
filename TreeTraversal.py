def printInorder(root):
    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# for traversing in preorder for a n-ary tree (tree with multiple children potentially):

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, r = [root], []
        while stack:
            node = stack.pop()
            if node != None:
                r.append(node.val)  # preorder
                for i in range(len(node.children)-1, -1, -1):  # traversing from the left
                    stack.append(node.children[i])
        return r
