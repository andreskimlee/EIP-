# 2d array written by sequence
# ex :
# [ [1,2,3 4 5], incrementing x axis until end of array. then you increment y axis til end of array
#   [4,5,6 4 5]. then you decrement x axis. Then you decrement y until you stop at 1
#   [7,8,9 4 5]
# ]

# height and width

# while row/col > 0


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
