indices = []
nums = [4,3,2,1]
k = 2
    
for i in range(len(nums)):
    binar = bin(i)[2:]
    cal = sum(int(bit) for bit in binar)
    
    if cal == k:
        indices.append(i)

result_sum = sum(nums[i] for i in indices)
print(result_sum)