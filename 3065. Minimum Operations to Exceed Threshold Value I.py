nums = [2,11,10,1,3]
k= 10
count = 0
for num in nums:
    if num < k:
        nums.remove(min(nums))
        count += 1
   
print(count)