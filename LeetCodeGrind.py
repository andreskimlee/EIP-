# 1304. Find N Unique Integers Sum up to Zero
# you include zero in odds else in evens you just start your incrementation of i as well as the negeative value. I used a deque to easily
# append left or to the right
# but you could also solve this using two pointers with a predetermined length of an array that starts inwards and expands outwards or vise versa


from collections import deque
from collections import OrderedDict


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        # if n = 5 [-2 -1,0, 1, 2] if odd you do.
        # if n = 4 [-2, -1, 1, 2] if even you dont account for the zero

        res = deque()

        if n % 2 == 0:
            i = 1
            while len(res) < n:
                res.appendleft(-i)
                res.append(i)
                i += 1

        if n % 2 != 0:
            res.append(0)
            i = 1

            while len(res) < n:
                res.appendleft(-i)
                res.append(i)
                i += 1

        return res


# 1374. Generate a String With Characters That Have Odd Counts

class Solution:
    def generateTheString(self, n: int) -> str:
        # Approach is to use a dictionary then iterate over the dictionary by a count of x depending on the length of requested str. easiest way is to just have two strings (since duplicates are alloweed)
        # for example : 4 you want to do anystring 3 times and 1 string 1 time
        # this logic works for 4000 (3999) strings of letter A and 1 b
        # for odd numbers. you can simply just return the letter A 3999 times.

        letterA = 'a'
        letterB = 'b'
        res = ""
        if n % 2 == 0:

            for _ in range(n - 1):
                res += letterA
            res += letterB

        else:

            for _ in range(n):
                res += letterA

        return res

# 1370 increasing decreasing string


class Solution:
    def sortString(self, s: str) -> str:
        n = len(s)
        s = sorted(s)
        od = OrderedDict()

        for i in range(n):
            if s[i] not in od:
                od[s[i]] = 1
            else:
                od[s[i]] += 1

        result = ''
        key_list = od.keys()
        while len(result) < n:
            for key in key_list:
                if od[key] > 0:
                    result += key
                    od[key] -= 1

            temp_str = ''
            for key in key_list:
                if od[key] > 0:
                    temp_str += key
                    od[key] -= 1
            result += temp_str[::-1]

        return(result)

# 832. Flipping an Image


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # brute force approach just reverse each element then invert it

        # [1,1,0] # [1,0,0] you can create a empty array Then traverse backwards while inserting into your empty array.

        res = []

        for num in A:
            temp = []
            i = len(num) - 1
            while i >= 0:
                if num[i] == 0:
                    temp.append(1)
                else:
                    temp.append(0)
                i -= 1
            res.append(temp)

        return res


# 590. N-ary Tree Postorder Traversal


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        res = deque()
        while stack:

            currNode = stack.popleft()
            res.appendleft(currNode.val)
            if currNode.children:
                a = len(currNode.children)
                for i in range(0, a):
                    stack.appendleft(currNode.children[i])

        return list(res)

# 1441. Build an Array With Stack Operations


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        numsList = (list(range(1, n + 1)))

        res = []

        i = 0
        j = 0
        while i < len(numsList) and j < len(target):

            res.append("Push")

            if numsList[i] == target[j]:
                i += 1
                j += 1
            else:
                res.append("Pop")
                i += 1
        return res


# 811. Subdomain Visit Count
# approach make a dictionairy of all words traversing backwards from the element in the cpdomains. then you can just check
# if the  key already exists in the dict then you add the current value to the value otherwise you set it equal to the amt which
# is defined in the string


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

        #          #google : 900
        #             mail: 901
        #             com : 951
        #             yahoo : 50
        #             intel : 1
        #             wiki: 1
        #             org: 1

        domainDict = {}

        dups = set()

        for domain in cpdomains:
            partsD = domain.split(" ")
            amt = partsD[0]
            allWords = partsD[1].split(".")
            print(allWords)
            for i in range(len(allWords) - 1, -1, -1):
                wordToAdd = ".".join(allWords[i:])
                print(wordToAdd)
                if wordToAdd in domainDict:
                    domainDict[wordToAdd] += int(amt)
                else:
                    domainDict[wordToAdd] = int(amt)

        res = []
        for key in domainDict:
            val1 = domainDict[key]
            val2 = key
            resStr = ""
            resStr += str(val1) + ' ' + val2
            res.append(resStr)

        return res
    # 922. Sort Array By Parity II
    class Solution:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # given half are odd and half are even, the greedy approach is to split it and just alternate between taking from each array until it is equal to the length of the original array.
        res = []
        mid = len(A) // 2

        even = []
        odd = []
        # because we dont know if the array is sorted with half even or half odd.
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])

        return res
