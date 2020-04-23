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
    # print(dp)
    return ["NO", "YES"][dp[len(a)-1][len(b)-1]]

# Constraints
# if there exists a letter in B that is capital and does not exist in a, it is impossible.
# My approach is iterate over B. IF letter in a or if it is lowercase, we know we can mark it as safe.


[[True, 0, 0, 0, 0],
 [False, True, 0, 0, 0],
 [False, True, True, 0, 0],
 [False, True, True, False, 0],
 [False, False, False, True, False],
 [False, False, False, False, True]]

# print(abbreviation('AbcDE', 'ABDE'))

# The Knapsack problem
# example input = [[$60, 5oz], [$50, 3oz]. [$70, 4oz], [$30, 2oz]] ==> ($80)  (3oz 20oz) given 5 oz constraint
# return dollar amount.


class Clock:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


# example input = [[$60, 5oz], [$50, 3oz]. [$70, 4oz], [$30, 2oz]] ==> ($80)  (3oz 20oz) given 5 oz constraint
def knap_sack(clocks, weight_limit):

    # outer for loop is the row    inner for loop is the col
    tabBoard = [[0 for i in range(weight_limit + 1)]
                for i in range(len(clocks) + 1)]
    # x represents the clock
    for x in range(1, len(clocks)+1):
        # y represents the weight constraint
        for y in range(1, weight_limit + 1):
            clock = clocks[x - 1]
            # print(clock.weight)
            # print(x)
            if clock.weight > y:
                tabBoard[x][y] = tabBoard[x - 1][y]
            else:
                tabBoard[x][y] = max(
                    tabBoard[x - 1][y], (clock.value + tabBoard[x - 1][y - clock.weight]))
    return tabBoard[-1][-1]

#            0, 1, 2,  3 ,  4 ,  5
#          [0, 0, 0,   0,   0,   0]
# $60/5 oz [0, 0, 0,   0,   0, $60]
# $50/3 oz [0, 0, 0, $50, $50, $60] $50 +
# $70/4 oz [0, 0, 0, $50, $70, $70]
# $30/2 oz [0, 0, 30, $50, $70,$80]


arr = [[60, 5], [50, 3], [70, 4], [30, 2]]
arr2 = [[65, 20], [35, 8], [245, 60], [195, 55], [65, 40], [150, 70], [275, 85], [155, 25], [
    120, 30], [320, 65], [75, 75], [40, 10], [200, 95], [100, 50], [220, 40], [99, 10]]
clocks = []

for ele in arr2:
    clocks.append(Clock(ele[1], ele[0]))

# print(clocks[0].weight)
# print(clocks[0].value)

# print(knap_sack(clocks, 130))


# Timne complexity / space = o(m*n)

# Count the number of score combinations.

# input = [2,3,7], 12 output should be 4

def calcCombos(num_plays, total_score):
    # num_plays = [2,3,7]
    dp = [[0 for i in range(total_score + 1)] for i in range(len(num_plays))]

    for i in range(len(num_plays)):
        for j in range(total_score + 1):
            play = num_plays[i]
            if j == play:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - num_plays[i]]

    return dp[-1][-1]

# [[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
# [0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3],
# [0, 0, 1, 1, 1, 1, 2, 1, 2, 3, 3, 3, 4]]


arr = [2, 3, 7]


#  A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

# Decode variations

# input:  S = '1262'
# output: 3
# explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.

# 1262
#         /\
# [1][262]  [12][62] at each decision, you either take the integer next to you or you continue without doing so.

counter = 0


def decodeVariations(S, memo = {}):
  if len(S) == 0:
    return 1 
  if S in memo: return memo[S]

  takeOne, takeTwo = 0,0
  
  if int(S[:2]) >= 10 and int(S[:2]) <= 26:
    takeTwo = decodeVariations(S[2:], memo)
  if int(S[:1]) >= 1 and int(S[:1]) <= 9:
    takeOne = decodeVariations(S[1:], memo)
  
  memo[S] = takeOne + takeTwo
  
  return memo[S]  