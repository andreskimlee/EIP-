# find rectangleIntersection

# Write a Program that takes two strings and computes
# the minirnum number of edits needed to transform the first string into the second string.

# an edit constitutes (inserting, deleting, editing)
v                v
# sunday to #sunday => 1 (a => u) + 1 ( a to u) + 1 (t to n) + 2 deletes (u and r)

# orthorse to orchestra => 8

# in backtracking at each letter:

# Step 1.: Find comanalities + it has to be sequential
# Step 2: edit or delete.

