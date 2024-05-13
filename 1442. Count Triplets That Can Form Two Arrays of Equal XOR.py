def count_triplets(arr):
    n = len(arr)
    xor_prefix = [0] * (n + 1)
    for i in range(n):
        xor_prefix[i + 1] = xor_prefix[i] ^ arr[i]

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j, n):
                a = xor_prefix[j] ^ xor_prefix[i]
                b = xor_prefix[k + 1] ^ xor_prefix[j]
                if a == b:
                    count += 1
    return count

# Example usage:
arr = [1,1,1,1,1]
print(count_triplets(arr))
