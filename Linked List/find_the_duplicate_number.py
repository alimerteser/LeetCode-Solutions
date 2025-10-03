from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = nums[abs(nums[i]) - 1]
            if num < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1

        return -1
