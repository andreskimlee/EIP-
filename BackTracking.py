# Generate Permutations  [2,3,5,7]


def genPerm(arr):
    all_perms = []

    def permutations(arr, perm):
        if len(arr) == 0:
            all_perms.append(perm[:])

        for ele in arr:
            perm.append(ele)
            decisionPool = arr[:]
            decisionPool.remove(ele)
            permutations(decisionPool, perm)
            perm.pop()

    permutations(arr, [])
    return all_perms


print(genPerm([2, 3, 5, 7]))

