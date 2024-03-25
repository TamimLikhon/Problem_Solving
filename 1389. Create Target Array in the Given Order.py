nums = [1]
index = [0]

target = []


for i in range(len(nums)):
    if index[i] == len(target):
        target.append(nums[i])
    else:
        target.insert(index[i], nums[i])

print(target)