# (apple, bannana, apple, apple, dog, cat, apple, dog, banana, apple, cat, dog)
# and the set {banana,cat}
# output is 3  (banna, apple, cat)

import math
from collections import Counter


def smallestSubArr(arr, keys):
    length_of_sub = float('inf')

    for idx, ele in enumerate(arr):
        curr_length = 1

        if ele in keys:
            words_to_cover = set(keys)
            while words_to_cover and idx < len(arr):
                if arr[idx] in words_to_cover:
                    words_to_cover.remove(arr[idx])
                curr_length += 1
                idx += 1
            length_of_sub = min(curr_length, length_of_sub)
    return length_of_sub


arr = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat',
       'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keys = {'banana', 'cat'}

# print(smallestSubArr(arr, keys))


# Photo Day -1
# Takes input two teams. Height of players in the teams, and checks to see if it is possible to place players to take a photo


# [5, 6, 7, 8, 9]
# [3, , 6, 5, 10]

# 5, 6, 7, 8
# 3, 5, 6, 10


# Write a program which takes as input an array of disjoint closed intervals with
# integer endpoints, sorted by increasing order of left endpoint, and an interval to be added,
# and returns the union of the intervals in the array and the added interval. Your result should be expressed
# as a union of disjoint intervals sorted by left endpoint.


# arr is sorted by left endpoint.

# [[-4, -1],[0,2],[1,8] [3,6], [7,9], [11,12],[14,17]}  #  [1,8] => [[-4, -1][0,9][11,12][14,17]]
# Step 1 : insert the interval
# Step 2: calculate union
#    iterate,
# start, CurrEnd
# nextStart > end then i know that union ended. (Push that interval)
# start  = 0, 2 end
# next iteration end becomes 8 then 9
# [start, end]
def mergeIntervals(arr, interval):
    newUnions = []
    appended_arr = insertInterval(arr, interval)

    start = appended_arr[0][0]
    end = appended_arr[0][-1]
    for i in range(len(arr)-1):
        curr_start = appended_arr[i][0]
        curr_end = appended_arr[i][1]

        next_start = appended_arr[i+1][0]
        next_end = appended_arr[i+1][1]

        if next_start > curr_end and start > next_start:
            print(next_start, curr_end)
            newUnions.append([start, end])
            start = float('inf')
            end = float('-inf')
        else:
            start = min(curr_start, start)
            end = max(curr_end, end)

    return newUnions


def insertInterval(arr, interval):
    startPoint = interval[0]
    for i in range(len(arr)):
        currStart = arr[i][0]
        nextStart = arr[i + 1][0]
        if currStart <= startPoint <= nextStart:
            arr.insert(i+1, interval)
        break
    return arr


arr = [[-4, -1], [0, 2], [1, 8], [3, 6], [7, 9], [11, 12],
       [14, 17]]  # [1,8] => [[-4, -1][0,9][11,12][14,17]]
interval = [1, 8]

print mergeIntervals(arr, interval)


def shifted_arr_search(shiftArr, num):
    pass  # your code goes here
    # [9, 12, 17, 2, 4, 5], num = 17

    leftPointer = 0
    rightPointer = len(shiftArr) - 1

    while leftPointer <= rightPointer:
        pivot = (leftPointer + rightPointer) // 2
        if shiftArr[pivot] == num:
            return pivot

        elif num > pivot and num > shiftArr[rightPointer]:
            rightPointer = pivot - 1

        elif num < pivot and num < shiftArr[leftPointer]:
            leftPointer = pivot + 1

        elif num > pivot and num <= shiftArr[rightPointer]:
            leftPointer = pivot + 1

        elif num < pivot and num >= shiftArr[leftPointer]:
            rightPointer = pivot - 1

    return -1

# You are given an array of student objects.
# Each student has an integer-valued age field that is
# to be treated as a key. Rearrange the elements of the
# array so that students of equal age appear together.
# The order in which diffurent ages appear is not important.
# How would your solution change if ages have to appear in sorted order?

# ex :
# student {
#  age : 10
# }


class Student:
    def __init__(self, age):
        self.age = age


def studentSort(arr):
    arr.sort(key=lambda x: x.age)

    return arr
    # n log n

# second approach. use a OrderedDict. sort the keys, append

# create a set from arr => unique values


def studentAdjacent(arr):
    def fun(n):
        return n.age

    adef = []
    abc = Counter(list(map(fun, arr)))
    for key in abc:
        adef += ([key] * abc[key])

    return adef


arr = [14, 12, 11, 13, 13, 14]
obj = []

for ele in arr:
    obj.append(Student(ele))

print(studentAdjacent(obj))


# [14, 12, 11, 13, 13, 14] => [11, 12, 13, 13, 14, 14]


# def addition(n):
#     return n + n

# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))
