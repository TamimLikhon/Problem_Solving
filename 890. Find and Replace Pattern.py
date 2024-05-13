def findAndReplacePattern(words, pattern):
    def is_match(word, pattern):
       return len(set(word)) == len(set(pattern)) == len(set(zip(pattern , word)))

    return [word for word in words if is_match(pattern, word)]

# Example usage:
words = ["a","b","c"]
pattern = "a"
print(findAndReplacePattern(words, pattern))  # Output: ["a"]
