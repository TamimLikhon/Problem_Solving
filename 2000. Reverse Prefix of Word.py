class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        if idx == -1:
            return word     
        rever_seg = word[:idx + 1][::-1]
        result = rever_seg + word[idx+1:]
        return result