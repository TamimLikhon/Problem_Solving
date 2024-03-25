nums = [1, 2, 3, 4]

result = []
for i in range(0, len(nums), 2): # pair - 0,2,4...n-2
    freq = nums[i]
    val = nums[i+1]
    result.extend([val] * freq)

print(result)
