from collections import defaultdict

def group_anagrams(strs):
    anargarms = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anargarms[sorted_word].append(word)
    return list(anargarms.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(strs)
print(output)