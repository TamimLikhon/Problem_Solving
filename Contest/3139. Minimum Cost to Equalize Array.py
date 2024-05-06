nums = [2, 3, 3, 3, 5]
cost1 = 2
cost2 = 1

count = 0
tar = max(nums)
for i in range(len(nums)):
    while nums[i] < tar:
        if i+1 < len(nums) and nums[i+1] < tar:
            nums[i] += cost1
            nums[i+1] += cost2
            count += 1
        else:
            nums[i] += cost1
            count += 1

print("Number of increments:", count)
print("Modified list:", nums)
