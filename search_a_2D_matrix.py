from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        low, high = 0, len(matrix) - 1
        row = None
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        if row is None:
            return False

        low_row, high_row = 0, len(row) - 1
        while low_row <= high_row:
            mid_row = low_row + (high_row - low_row) // 2
            if row[mid_row] == target:
                return True
            elif row[mid_row] < target:
                low_row = mid_row + 1
            else:
                high_row = mid_row - 1

        return False
