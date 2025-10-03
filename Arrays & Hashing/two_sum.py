class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in d:
                return [d.get(x), i]
            else:
                d[num] = i
