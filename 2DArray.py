# 2d array written by sequence
# ex :
# [ [1,2,3 4 5], incrementing x axis until end of array. then you increment y axis til end of array
#   [4,5,6 4 5]. then you decrement x axis. Then you decrement y until you stop at 1
#   [7,8,9 4 5]
# ]

# height and width

# while row/col > 0


import math


def spiralArr(matrix):
    traversedArr = []
    counterX = 0
    counterY = 0
    length = len(matrix[0]) - 1
    counterLeft = length

    while counterX <= length:
        traversedArr.append(matrix[0][counterX])
        counterX += 1

    while counterY <= length:
        traversedArr.append(matrix[counterY][length])
        counterY += 1

    while counterLeft >= 0:
        print(matrix[length-1])
        traversedArr.append(matrix[length][counterLeft])
        counterLeft -= 1

    print(traversedArr)


arr1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ]

# 0,0 to 0 2, then 0,1 to 2, 2 then 2,2 to 2,0, then 2,0 to 0,0
coord = [0, 0], [0, 1], [0, 2]
[1, 0], [1, 1], [1, 2]
[2, 0], [2, 1], [2, 2]


# matrix[x][y]
# if y == 0:
#     y+= 1
#     spiralArr(matrix, x, y)


spiralArr(arr1)


def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))


def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True


def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True

# used to calculate the sub grids to ensure theyre unique.


def is_square_valid(self, board):
    for i in (0, 3, 6):  # iterates each element 0 to 3 to 6
        for j in (0, 3, 6):  # iterates each element 0 to 3 to 6
            square = [board[x][y]
                      for x in range(i, i + 3) for y in range(j, j + 3)]
            # this is equal to the above,
            # square = for x in range(i,i +3):
            # for y in range(j,j+3):
            # square = board[x][y]
            #
            if not self.is_unit_valid(square):
                return False
    return True


def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)


# [-14, 10, 2 , 108, 243 , 285 ,285, 285 ,401]
# if given key 285 should return first found idx.
# should return -1
# method --> sorted arr, with a key

# pivot = len(arr) / 2 floored


def findKey(arr, target, side=[]):
    pivotidx = math.floor(len(arr) / 2)
    leftSide = side[0:pivot]
    rightSide = side[pivot:len(arr)]

    # while loop would iterate k times. (Depending on amount of duplicates)
    if arr[pivot] == target:
        i = 0
        while arr[pivot] == arr[pivot + i]:
            i += 1
        return (pivot + i)

    if arr[pivot] > target:
        findKey(arr, target, leftSide)

    if arr[pivot] < target:
        findKey(arr, target, rightSide)


def findKey(arr, target, leftSide=0, rightSide=-1):
    pivotIdx = math.floor(len(arr[leftSide:rightSide]) / 2)

    if arr[pivot] > target:
        rightSide = pivot
        findKey(arr, target, leftSide, rightSide)

    if arr[pivot] < target:
        leftSide = pivot
        findKey(arr, target, leftSide, rightSide)


# Given two sparse matrices A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.
# Example:
# Input:
A = [
    [1, 0, 0],
    [-1, 0, 3]
]
B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
# Output:
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


def calcMatrix(a, b):

    result = [[0 for i in range(len(b))] for i in range(len(a))]
    print(result)

