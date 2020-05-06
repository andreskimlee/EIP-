def printInorder(root):
    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


[0, 0], [0, 1], [0, 2]

ships = 3

[0, x, 0, 0, 0, 0, x]
[0, x, 0, 0, 0, 0, x]
[0, x, 0, 0, 0, 0, x]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
