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


import heapq
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


# k number of stars closest to earth. return in an array


def findKthSmallestEle(stars, k):
    max_heap = []
    for star in stars:
        totalDistance = sum(star)
        heapq.heappush(max_heap, -totalDistance)
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    return max_heap.sort()

# maxheap = [3, 1, 2, 1] k = 3


# heapq.heappop()

def LCA(root, x, y):
    if (root == None):
        return None
    if root.val == x or root.val == y:
        return root

    leftRes = LCA(root.left, x, y)
    rightRes = LCA(root.right, x, y)

    # l
    if leftRes == None:
        return rightRes

    if rightRes == None:
        return leftRes

    # this case only gets hit if both left and right res are not null in which that means
    # the root you are on is the LCA.
    return root

# find the kth largest element
# the trick is to do it in nlogk times.
# You can do this in O(n log k), using O(k) extra space by modifying the algorithm slightly. I'm not a Python programmer, so you'll have to translate the pseudocode:
# create a new min-heap
# push the first k nums onto the heap
# for the rest of the nums:
#     if num > heap.peek()
#         heap.pop()
#         heap.push(num)

# // at this point, the k largest items are on the heap.
# // The kth largest is the root:

# return heap.pop()
# The key here is that the heap contains just the largest items seen so far. If an item is smaller than the kth largest seen so far, it's never put onto the heap. The worst case is O(n log k).

# Actually, heapq has a heapreplace method, so you could replace this:

#     if num > heap.peek()
#         heap.pop()
#         heap.push(num)
# with

#     if num > heap.peek()
#         heap.replace(num)


def isTreeBst(h, Upper=0, Lower=0):
    Upper = h.val
    Lower = h.val

    if not h:
        return True

    if h.left.val < Lower and h.left.val > h.val:
        Lower = h.left.val
    elif h.right.val > Upper and h.right.val > h.val:
        Upper = h.left.val
    else:
        return True

    return isTreeBst(h.left, Upper, Lower) and isTreeBst(h.right, Upper, Lower)

# in order traversal
# all keys are unique


def isBST(root, upper=float('inf'), lower=float('-inf')):
    if root == None:
        return True

    elif lower > root.val > upper:
        return False

    return isBST(root.left, root.val, lower) and isBST(root.right, upper, root.val)

# inorder traversal
# left root right [1,2,3,4,5]
# see if that list is sorted

# headnode.

    # 20
#     /  \
#    15   25
#    / \
#   10 16

# [20,15,10,16,25] preorder
# [10,15,16,20,25] in order


def traverseTreeBST(preorder, inOrder=[]):  # preorder sequence
    if not inOrder:
        inOrder = sorted(sequence)

    if len(inOrder) == 1:
        return inOrder[0]

    root = preorder[0]
    rootIdx = inOrder.index(root)

    root.left = traverseTreeBST(preorder[1:-1], inOrder[:rootIdx])
    root.right = traverseTreeBST(inOrder[rootIdx:-1])
