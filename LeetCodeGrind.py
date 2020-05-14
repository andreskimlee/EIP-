# 1304. Find N Unique Integers Sum up to Zero
# you include zero in odds else in evens you just start your incrementation of i as well as the negeative value. I used a deque to easily
# append left or to the right
# but you could also solve this using two pointers with a predetermined length of an array that starts inwards and expands outwards or vise versa


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
