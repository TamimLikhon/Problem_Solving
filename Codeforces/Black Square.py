weights = list(map(int, input().split()))

s = input()

total_weight = 0

for char in s:
    strip_index = int(char) - 1
    total_weight += weights[strip_index]

print(total_weight)



#bujhi nai
