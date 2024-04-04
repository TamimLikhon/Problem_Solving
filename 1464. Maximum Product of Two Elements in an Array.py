nums = [3,4,5,2]
max1 = max(nums)
nums.remove(max1)
max2 = max(nums)

print( (max1 - 1) * (max2 - 1) )