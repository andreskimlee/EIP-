# For example, if the input is 16, return 4; if the input is 300,
# return 17, since 17^2 = 289 < 300 and 18^2 = 324 > 300.

# if you sqrt the input and if mod  == 0 then return

# ex sqrt of 300 = 17.3 <-- check if its a whole numb just return


import math


def squareRootGreater(num1, side=[]):
    # math.sqrt(num1)
    # if len(side) == 0:
    #     return -1
    # else:
    #     allNums = side

    allNums = list(range(1, num1))
    left = 0
    right = len(allNums)
    while left < right:
        middle = ((left + right) // 2)

        if (allNums[middle] * allNums[middle]) <= num1:
            left = middle + 1
        else:
            right = middle

    return (allNums[left - 1])


print(squareRootGreater(300))
print(squareRootGreater(16))
print(squareRootGreater(21))
print(squareRootGreater(25))
