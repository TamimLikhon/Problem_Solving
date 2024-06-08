class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        count = 0

        for word in words:
            reverse_word = word[::-1]
            if reverse_word in seen:
                count += 1
                seen.remove(reversed_word)
            else:
                seen.add(word)

        return count