def reverse_word(s):
    words = s.split()
    m =[word[::-1] for word in words]
    return ' '.join(m)

s = "Let's take LeetCode contest"
result = reverse_word(s)
print(result)