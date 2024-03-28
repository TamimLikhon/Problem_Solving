arr = [10,11,12]
count = 0

for i in range(len(arr)):
    subarray_sum = 0
    for j in range(i, len(arr)):
        subarray_sum += arr[j]
        if (j + i) % 2 == 0:
            count += subarray_sum

print("Output: ", count)