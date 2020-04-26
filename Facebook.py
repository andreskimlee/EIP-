# [6,2,1,5,4,3,0]
#


def nextPermutation(self, nums):
    i = j = len(nums)-1

    # [6,2,1,5,4,3,0] both i and j are at 0

    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    # i will stop at 1. if there are no nums i will stop at 0

    if i == 0:   # nums are in descending order
        nums.reverse()
        return

    # this is used to capture the edge case where the permutation is on its last permutation.

    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1

    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


# [6,2,1,5,4,3,0] => reversed it would look like this [0,3,4,5,1,2,6] start in reversed because from the end you want to see where the descneding numbers
# end. This means the next permutation is at this point.

# In this example, 1 is the point where the descension began. Now you need to swap the next number greater than 1 which is 3.

# [0,1,4,5,3,2,6]
#
# next step. if you slice from [0,1,4,5] and add it to the swapped of 326  which equals 623
# you get [6,2,3] + [0,1,4,5] --> [6,2,3,0,1,4,5]
