# Binary Tree height balanced not perfect or complete. Difference is 1 or 0
# Returns a bool (true if height-balanced, else false)

# Counter, increment counter at each level of progression.
# node --> node.left / node.right
# if node.left go left if node.right go right.
# PST left right middle
# helper function


# def binaryTreeHeight(root):

#    if (not root):
#         return True

#     leftSide = CalcHeight(root.left)
#     rightSide = CalcHeight(root.right)

#     maxDiff = abs(leftSide - rightSide)

#     if maxDiff > 1:
#         maxDiff = False
#     else:
#         maxDiff = True

#     return maxDiff and binaryTreeHeight(root.left) and binaryTreeHeight(root.right)

# compare height of left root , right root.


from heapq import heappush


def CalcHeight(node):
    if (not node):
        return -1

    1 + max(CalcHeight(node.left), CalcHeight(node.right))

##########################################################

# 10.4

# consider a coordinates system milkyway where earth is at (0,0,0)
# Model stars as points and assume distances are in light years
# milky way consists of 10^12 stars
# star A
# [x, y, z] ==> total distance apart from earth.

# earth --> star1 --> star2 -- etc
##
# nLogn
# traverse arr until k

# how would you compute k stars closest to earth. if k = 10

# kth smallest element in a 2d array. [[x,y,z], [x2,y2,z2]]
            # max heap
    #         dummy node
    #         /   \
    #     100       50
    #     /           \
    #    40           30

# stars are 2d array of cooridinates


def findKthSmallestEle(stars, k):
    max_heap = []
    for star in stars:
        totalDistance = sum(star)
        heappush(max_heap, totalDistance)
    print(max_heap)
    return max_heap


abc = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

findKthSmallestEle(abc, 3)
