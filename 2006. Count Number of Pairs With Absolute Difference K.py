nums = [1,2,2,1]
k = 1
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if abs(nums[i] - nums[j] == k):
            count += 1

print("Output: ", count);