s = "(1+(2*3)+((8)/4))+1"

n = len(s)
current_depth = 0
max_depth = 0

for char in s:
    if char == '(':
        current_depth += 1
        if current_depth > max_depth:
            max_depth = current_depth 
    
    elif char == ')':
        current_depth -= 1
    

print(max_depth)

