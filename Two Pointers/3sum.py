class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, start in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            while right > left:
                if nums[right] + nums[left] > -start:
                    right -= 1
                elif nums[right] + nums[left] < -start:
                    left += 1
                else:
                    if [start, nums[left], nums[right]] not in res:
                        res.append([start, nums[left], nums[right]])
                    right -= 1

        return res
