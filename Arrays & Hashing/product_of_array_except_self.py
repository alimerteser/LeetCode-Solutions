from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums), 1):
            res[i] = res[i-1] * nums[i-1]

        res2 = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            res2[i] = res2[i + 1] * nums[i + 1]

        ret = [1] * len(nums)
        for i in range(len(nums)):
            ret[i] = res[i] * res2[i]
        return ret
