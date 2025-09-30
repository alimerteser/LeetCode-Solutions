from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low < high:
            mid = low + (high - low) // 2  # mid = k
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours > h:
                low = mid + 1
            else:
                high = mid
        return low