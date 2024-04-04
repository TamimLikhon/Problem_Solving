nums = [4,2,5,9,7,4,8]
sorted_nums = sorted(nums)
print(sorted_nums)

product_difference = (sorted_nums[-1] * sorted_nums[-2]) - (sorted_nums[0] * sorted_nums[1])

print("Product Difference:", product_difference)
