import itertools

def findingsubsets(nums):
    return [subset for i in range(len(nums) + 1)
    for subset in itertools.combinations(nums, i)
    ]


nums = [1,2,3]

result = findingsubsets(nums)

print(result)