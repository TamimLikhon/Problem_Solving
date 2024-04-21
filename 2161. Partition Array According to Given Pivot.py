def dfs(nums, pivot):
    # Base case: if nums is empty, return an empty list
    if not nums:
        return []

    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in nums:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    # Recursively apply dfs on the three partitions
    return dfs(less_than_pivot, pivot) + equal_to_pivot + dfs(greater_than_pivot, pivot)

nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

ans = dfs(nums, pivot)
print(ans)
