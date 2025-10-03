from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count the frequencies
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Step 2: Generate bucket list according to frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        # Step 3: Pick k elements starting from the highest frequency
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
