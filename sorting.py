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
