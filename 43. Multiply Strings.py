def multiply(num1, num2):
    a = 0
    for i in range(len(num1)):
            a = a*10 + int(num1[i])
    print("value of a: ",a)    
    b = 0
    for i in range(len(num2)):
            b = b*10 + int(num2[i])
    print("value of b: ",b)

    return str(a * b)

num1 = "2"
num2 = "3"
result = multiply(num1, num2)

print(result)