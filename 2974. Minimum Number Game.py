nums = [5, 4, 2, 3]
res = []
nums = sorted(nums)
for i in range(0, len(nums), 2):
    res.extend(nums[i:i+2][::-1])
print(res)