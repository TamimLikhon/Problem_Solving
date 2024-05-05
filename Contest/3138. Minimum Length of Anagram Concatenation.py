class Solution:
    def minAnagramLength(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for count in char_count.values():
            if count > 1:
                return len(s)
        
        return len(set(s))

# Example usage
solution = Solution()
s = "xxe"
print(solution.minAnagramLength(s))  # Output: 3
