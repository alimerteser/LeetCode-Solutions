from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        half = (len(nums1) + len(nums2)) // 2
        r = len(nums1)
        l = 0
        while r >= l:
            m = l + (r - l) // 2
            m2 = half - m
            max1 = nums1[m-1] if m != 0 else float("-inf")
            min1 = nums1[m] if m != len(nums1) else float("inf")
            max2 = nums2[m2-1] if m2 != 0 else float("-inf")
            min2 = nums2[m2] if m2 != len(nums2) else float("inf")

            if max2 > min1:
                l = m + 1
            elif max1 > min2:
                r = m
            else:
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return min(min1, min2)
                else:
                    return (max(max1, max2) + min(min1, min2)) / 2
