# cycle linked list. Singly linked list returns null if no cycle.
# if cycle exists return the start of the cycle or roothead.
# you dont know length of the list

# [a-->b-->c--> a ] should return a.
# [a-->b-->c] should return null

# visited = {
#   a : b
#   b : c
#   c : a ## flag. The flag is set to true if it points to another key.
# }

# visited = {
#   a : b
#   b : c
#   c : none
# }


# if [key] does not exist visited[key] = something


def TestCyclicity(head):
    main_head = head
    visited = {}
    currHead = head
    isCyclicity = False
    while currHead:
        if currHead not in visited:
            visited[currHead] = currHead.next
            currHead = currHead.next
        elif visited[currHead] in visited:
            isCyclicity = True
            break

    if isCyclicity:
        return main_head
    else:
        return null

    # Their approach two seperate numerators and you iterates faster one that is slower
