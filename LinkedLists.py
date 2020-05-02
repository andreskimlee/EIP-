# consider two linked lists. each node val. list is sorted. ascending.
# merged two lists, sorted.
# list1 [2,5,7] list2 [3,11] --> 2,3,5,7,11 -- > null
#
# start at the header. compare which header is less.
# h1next = h1next.next / h2next = h2next.next / h1Next / h2next  / currHead


def Merge_Two_Linked_List(h1, h2):
    # a while loop.
    # if curr1.val < curr2.val
    # then h1.next points to h2
    # then we change currhead to h2.
    # Next iteration we compare 5 and 3 which are essentially
    # curr1 = curr1.next / curr2 = curr2.next
    # a if condition else b

    curr_1 = h1
    curr_2 = h2
    main_head = h1 if h1.val > h2.val else h2
    curr_head = main_head
    while curr_1 or curr_2:
        if curr_1.val < curr_2.val:
            curr_head.next = curr_2
            curr_head = curr_2

        else:
            curr_head.next = curr_1
            curr_head = curr_1

        curr_1 = curr_1.next
        curr_2 = curr_2.next

    curr_head.next = Null

    return main_head


def returnKthLastEle(h1, k):
    # approach if we know the length of the list we can find the kth last element. Example
    # lets say you are given a linked list 0 -- > 1 --> 2 --> 3 --> 4
    # use two pointers. One fast one slow with k distance apart.
    # Example k = 2 (2nd to last element) should return


# Reverse a singly sublist

# input

def revSublist(h1, num1, num2):

# example, 2, 4
# 1 --> 2 -- > 3 --> 4

# 1 <= 2 <= 3 <= 4
# 1 ==> none
# 2 => 1 => none
#


#  1--> 4 --> 3 --> 2
    slow_pointer = h1
    fast_pointer = h1
    distance_apart = num2 - num1
    while distance_apart:
        fast_pointer = fast_pointer.next
        distance_apart -= 1

    curr = slow_pointer
    while curr:
            prev = curr
            curr = curr.next
        if slow_pointer.val == num1: 
            prev.next = revHelper(slow_pointer)
        
    return h1 
 




def revHelper(head): # 2 --> 3 --> 4 
                    # 2 <-- 3 <-- 4 
                    # 4 == > 3 ==> 2 
    prev = None
    curr = head 

    while curr.next:
        curr.next = prev
        prev = curr
        curr = curr.next 
    
    return curr 



# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a 
# doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, 
# and the successor of the last element is the first element.
## We want to do the transformation in place. After the transformation, ## 
# the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. 
# You should return the pointer to the smallest element of the linked list.
           
   [1,2,3,4,5, 1]


class Node:
    def __init__(self, val, next, prev):  
        self.val = val
        self.next = next
        self.prev = prev 
 


def convertBST(root)
    # BST 4    left root right 
    #    /\
    #   2   5 
    #  /\
    # 1  3

    prev = None
    curr = None

    def TraverseBST(root):
        
        if root == None:
            return 

        curr = root 

        left = TraverseBST(root.left)
        
        Node(root.val, left,)
        
        right = TraverseBST(root.right)

        return root 

    TraverseBST(root)

    





def treeToDoublyList(self, root: 'Node')
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)


        if not root:
            return None
        # the smallest (first) and the largest (last) nodes
        first, last = None, None

        
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first
Collap
