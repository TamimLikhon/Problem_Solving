nums = [10,4,8,3]
calc = 0
leftsum = [0] * len(nums)
for i in range(len(nums)):
    if i > 0:
        calc += nums[i-1]
    leftsum[i] = calc

rightSum = [0] * len(nums)
rightSum[-1] = 0
for i in range(len(nums) - 2, -1, -1):
    rightSum[i] = nums[i + 1] + rightSum[i + 1]

print("leftSum: ", leftsum)
print("RightSum: ", rightSum)

absolute_diff = [abs(leftsum[i] - rightSum[i]) for i in range(len(nums))]
print(absolute_diff)
