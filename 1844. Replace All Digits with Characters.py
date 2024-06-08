class Solution:
    def replaceDigits(self, s: str) -> str:
        s_list = list(s)
        
        for i in range(1, len(s), 2):
            char = s_list[i - 1]
            digit = int(s_list[i])
            s_list[i] = chr(ord(char) + digit)
        
        # Convert the list back to a string and return
        return ''.join(s_list)