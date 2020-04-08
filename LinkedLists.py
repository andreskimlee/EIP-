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
