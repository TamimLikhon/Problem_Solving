from functools import reduce
from operator import ior
from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(ior, nums)
