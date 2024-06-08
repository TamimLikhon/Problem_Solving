def makesmallpalindrome(s):
    n = len(s)
    s = list(s)
    l, r = 0, n - 1
    
    while l < r:
        if s[l] != s[r]:
            if s[l] < s[r]:
                s[r] = s[l]
            else:
                s[l] = s[r]
        
        l += 1
        r -= 1

    return ''.join(s)