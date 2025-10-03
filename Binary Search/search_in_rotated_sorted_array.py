from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:        # r returns the index which the array is cut
            m = l + (r - l) // 2

            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1

        if nums[m] <= target <= nums[len(nums) - 1]:
            high = len(nums) - 1
            low = r
        else:
            high = r - 1
            low = 0

        while high >= low:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
