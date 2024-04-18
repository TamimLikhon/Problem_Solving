boxes = "001011"
carry = []
n = len(boxes)

for i in range(n):
    operation = 0
    for j in range(n):
        if i != j and boxes[j] == '1':
            operation += abs(i - j)
    carry.append(operation)

print(carry)
