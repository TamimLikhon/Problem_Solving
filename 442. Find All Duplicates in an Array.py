class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = {}
        duplicates = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, freq in count.items():
            if freq > 1:
                duplicates.append(num)

        return duplicates
