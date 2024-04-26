nums = [3, 5, 2, 3]

# Sort the list in non-decreasing order
nums.sort()

# Initialize a variable to store the maximum sum
max_sum = 0

# Iterate over the list in pairs
for i in range(len(nums) // 2):
    pair_sum = nums[i] + nums[-(i + 1)]  # Sum of current pair
    max_sum = max(max_sum, pair_sum)  # Update max_sum if pair_sum is greater

print(max_sum)
