nums = [2,3,3,3,5]
cost1 = 2
cost2 = 1

count = 0
tar = max(nums)
for i in range(len(nums) - 1):
    nums[i] += cost1

print(nums)