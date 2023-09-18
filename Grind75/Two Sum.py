from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums[i+1:n]:
                result.append(i)
                result.append(nums[i+1:n].index(tmp) + i + 1)
        return result