from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                i=0
                while num+i in nums:
                    seen.add(num + i)
                    i+=1
                max_len = max(max_len, len(seen))
                seen = set()
        return max_len