def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(i, k) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
    
    return dp[n]

# Example usage
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
result = maxSumAfterPartitioning(arr, k)
print(result)
