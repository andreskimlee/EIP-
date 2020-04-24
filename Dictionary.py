# english lowercase letter. order is permutation of letter.
# given a sequence of words and order of alphabet. Return true if sorted lexigraphically
# input = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"" = output true
# words = ["apple","app"], order = "abcdefghijklmnop  qrstuvwxyz"
# verifying alien dictionairy.

# at each words index[i] if it doesnt exist from string[:]
# words should be in alphabetical order
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false


# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

def alienDict(inputStr, order):

    for i in range(len(inputStr) - 1):
        wordOne = inputStr[i]
        wordTwo = inputStr[i + 1]

        minLength = min(len(wordOne), len(wordTwo))

        for j in range(minLength):
            # print(wordOne[j], wordTwo[j])
            # print(order.index(wordOne[j]), order.index(wordTwo[j]))
            # print(order.index(wordOne[j]) > order.index(wordTwo[j]))

            if wordOne[j] == wordTwo[j]:
                continue
            elif order.index(wordOne[j]) > order.index(wordTwo[j]):
                return False
            else:
                break

        if len(wordOne) > len(wordTwo):
            return False

    return True


arr = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"


arr2 = ["hello", "leetcode"]
order2 = "hlabcdefgijkmnopqrstuvwxyz"

print(alienDict(arr2, order2))
print(alienDict(arr, order))

["kuvp", "q"]
"ngxlkthsjuoqcpavbfdermiywz" = > true


# def isAlienSorted(self, words, order):
#         for i in range(len(words) - 1):
#             current = words[i]
#             next_word = words[i + 1]
#             idx = 0
#             while idx < len(current):
#                 left = current[idx] if idx < len(current) else None
#                 right = next_word[idx] if idx < len(next_word) else None
#                 if not right:
#                     return False
#                 leftIdx = order.index(left)
#                 rightIdx = order.index(right)
#                 if leftIdx == rightIdx:
#                     idx += 1
#                 elif leftIdx < rightIdx:
#                     break
#                 else:
#                     return False


#         return True
