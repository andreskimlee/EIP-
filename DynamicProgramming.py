# Hacker Rank Question Find Max subset. Non contiguos subset.
# input example = [-2, 1, 3, -4, 5] ==> 8 [3,5]
# First step. Find all non contiguous subsets.
# use recursive backtracking here. REMEMBER 3 things
# 1. choice (Create a decision pool at each recursive call)
# 2. what are our constraints at each call stack.
# 3. goal ? (in this case when we have no decesions left to choose from)

from collections import deque


def findMaxSubSet(arr):
    a, b = 0, 0
    for num in arr:
        a = b
        # at -2 it will return 0. second iteration b = 1 and will return 1 third, is 3
        b = max(a, a + num, b, num)
    return b


def abbreviation(a, b):
    # a is the string given to us and b is the string to match
    # you can uppercase letters and delete all lowercases.
    # a = AbcDE and b = ABDE  => Yes
    # a = AbcDE and b = AFDE = > No

    a = "."+a
    b = "."+b

    dp = [[0]*len(b) for _ in range(len(a))]

    dp[0][0] = True

    for i in range(1, len(a)):
        for j in range(min(len(b), i+1)):
            print((i, j))
            dp[i][j] = a[i].islower(
            ) and dp[i-1][j] or a[i].upper() == b[j] and dp[i-1][j-1]
    print(dp)
    return ["NO", "YES"][dp[len(a)-1][len(b)-1]]

# Constraints
# if there exists a letter in B that is capital and does not exist in a, it is impossible.
# My approach is iterate over B. IF letter in a or if it is lowercase, we know we can mark it as safe.


print(abbreviation('AbcDE', 'ABDE'))
