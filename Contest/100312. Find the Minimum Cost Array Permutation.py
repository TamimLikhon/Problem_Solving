def min_score_permutation(nums):
    n = len(nums)
    perm = [0] * n
    visited = [False] * n
    
    for num in sorted(nums):
        best_pos = -1
        best_diff = float('inf')
        for i in range(n):
            if not visited[i]:
                diff = abs(i - num)
                if diff < best_diff:
                    best_diff = diff
                    best_pos = i
        perm[best_pos] = num
        visited[best_pos] = True
    
    return perm

# Example usage:
nums = nums = [0,2,1]
print(min_score_permutation(nums))
