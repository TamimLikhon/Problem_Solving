s = ")()())"
co_par1 = "()"

print(len(s),"Incorrect")
print(len(co_par), "Correct")

count = 0

if co_par in s:
    count +=1

print(count)
