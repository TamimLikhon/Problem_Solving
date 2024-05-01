from itertools import permutations
def perm(lst):
    l = list(permutations(lst))

    return l


lst = [1,2,3]

result = perm(lst)
print(result)

