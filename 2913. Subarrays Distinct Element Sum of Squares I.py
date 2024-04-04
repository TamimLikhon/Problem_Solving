nums = [1, 2, 1]

total = 0
for i in range(len(nums)):
    distinct_counts = {}
    for j in range(i, len(nums)):
        distinct_values = set(nums[i:j+1])
        count = len(distinct_values)
        distinct_counts[count] = distinct_counts.get(count, 0) + 1
    for count in distinct_counts:
        total += count * count * distinct_counts[count]

print(total)

