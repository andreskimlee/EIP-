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
