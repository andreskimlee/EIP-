# (apple, bannana, apple, apple, dog, cat, apple, dog, banana, apple, cat, dog)
# and the set {banana,cat}
# output is 3  (banna, apple, cat)

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

print(smallestSubArr(arr, keys))


# Photo Day -1
# Takes input two teams. Height of players in the teams, and checks to see if it is possible to place players to take a photo


[5, 6, 7, 8, 9]
[3, , 6, 5, 10]

5, 6, 7, 8
3, 5, 6, 10
