# Write a program which takes as input two sorted arrays, and returns a new array containing
# elements that are present in both of the input arrays. The input arrays may have duplicate entries,
# but the returned array should be free of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12>
# and (5,5,6,8,8,9,10,10), your output should be (5, 6, 8).

import bisect


def findIntersects(input1, input2):
    checkSet = set(input1)  # o(input1)
    arr = []
    # print(checkSet)
    for key in checkSet:  # o(m)
        # (logn) bsearch  // if you use key in input2 this is o(n)
        idx = bisect.bisect_left(input2, key)  # (logn)
        # This checks to see if the element is found in the input2.
        if (idx < len(input2) and input2[idx] == key):
            arr.append(key)  # (o(1))
    return arr


# print(findIntersects([2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
#                      [5, 5, 6, 8, 8, 9, 10, 10]))


#  idx = bisect_left(items, key)
#     if items[idx] != key:
#          return -1

#     return idx


# If it is odd, triple it and add one;
# if it is even, halve it. Repeat the process indefinitely. No matter what number you begin with, you
# will eventually arrive at 1.
# As an example, if we start with 11 get the sequence 11,34,17,52,26,13,40,20,10,5,16,8,4,2,1.

# Test n integers.
# given n integers [11]

# n is the max number.


def findNCollatz(kth):
    masterDict = set(HelperCollatz(kth))

    for i in range(1, kth):
        if i % 2 == 0:
            continue
        else:
            if i in masterDict:



def HelperCollatz(num):
    collatz_conj = [num]

    while collatz_conj[-1] != 1:
        if collatz_conj[-1] % 2 == 0:
            collatz_conj.append(collatz_conj[-1] // 2)
        else:
            collatz_conj.append(((collatz_conj[-1] * 3) + 1))

    return collatz_conj


print(collatz(1))
print(collatz(2))
print(collatz(3))
print(collatz(4))
print(collatz(5))
print(collatz(6))
print(collatz(7))
print(collatz(8))
print(collatz(9))
print(collatz(10))
# 50 --> 25 -->


# find the maximum subbarray for a given arrray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
