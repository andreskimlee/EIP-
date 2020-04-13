# Question :
# Write a program takes in integer array. Calc maximum amount of water
# [2, 2, 1, 3, 4, 4, 5, 6, 2 , 1 , 3, 1, 3, 2, 1, ,2, 4, 1] =>
# increment the left pointer if the different of curr pointer to next pointer is 0 or greater.
# next + 1 >= curr
# idx represents presents location
# [4, 16] <- indexes
# start with zero and end of the array.

import math


def findMaxArea(arr):
    leftPointer = 0
    rightPointer = len(arr) - 1
    ans = []
    maxArea = 0

    while leftPointer < rightPointer:
        totalwidth = abs(leftPointer - rightPointer)
        totalHeight = min(leftPointer, rightPointer)
        currArea = totalwidth * totalHeight
        maxArea = max(maxArea, currArea)
        if arr[leftPointer] >= arr[rightPointer]:
            rightPointer -= 1
        elif arr[rightPointer] >= arr[leftPointer]:
            leftPointer += 1

    return maxArea


arr = [2, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
print(findMaxArea(arr))


def compute_largest_rectangle(heights):
    maxArea = 0
    for i in range(0, len(heights)):
        for j in range(i, len(heights)):
            width = 1
            if heights[i] <= heights[j]:
                width += 1
            else:
                break
        maxArea = width * heights[i]
        print(width)
    return maxArea


heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
print(compute_largest_rectangle(heights))
