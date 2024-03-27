nums = [1,15,6,3]

digit_sum = 0
nums_sum = sum(nums)
for num in nums:
    num_str = str(num)

    for digit in num_str:
        digit_sum += int(digit)

final_sum = nums_sum - digit_sum

print(final_sum)