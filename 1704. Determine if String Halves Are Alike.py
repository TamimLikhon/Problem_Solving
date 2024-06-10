class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = n // 2
        fir_a = s[:a]
        las_a = s[a:]
        alike = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        count_fir = 0
        count_las = 0

        for char in fir_a:
            if char in alike:
                count_fir += 1

        for char in las_a:
            if char in alike:
                count_las += 1

        if count_fir == count_las:
            return True
        else:
            return False
