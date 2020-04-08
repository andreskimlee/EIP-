# do it in one pass
# example alice likes bob --> bob likes alice
# new str


def reverseWrds(str):
    revWord = ""
    allWords = str.split()  # o(n)
    while len(allWords) >= 1:  # o(1) for len and a while loop that is based on length of array lets say k. Total time complexity is o(n) + k
        revWord += allWords[-1] + " "
        allWords = allWords[0:-1]
    return revWord


ex1 = 'alice likes bob'

print(reverseWrds(ex1))


# def replace-and-remove(size, s):


# # Forward iteration: temove 'b's and count the number of 'a's
# 71,
# write-idx, a-count = 0, 0
# for i in range(size):
# if s[i] != 'b':
# sIwrite-idx] = stil
# write-idx += 1
# if s[i] == 'a':
# a-count += 1
# # Backward iteration: replace 'a's with
# cur-idx = write-idx-1
# write-idx += a-count - I
# final-size = write-idx + 1
# while cur-idx >= 0:
# if s [cur-idx] = - 'a':
# sIwrite-idx - 1: write-idx + 1]=
# write-idx -= 2
# else:
# sIwrite-idx] = sIcur-idx]
# nrite-idx -= 1
# cur-idx -= 1
# return final-size
