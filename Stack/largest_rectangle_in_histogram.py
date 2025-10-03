class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        left_boundaries = [-1] * len(heights)
        right_boundaries = [len(heights)] * len(heights)

        left_stack = []
        right_stack = []
        for i in range(len(heights)):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            if left_stack:
                left_boundaries[i] = left_stack[-1]
            left_stack.append(i)
        for i in range(len(heights)-1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if right_stack:
                right_boundaries[i] = right_stack[-1]
            right_stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            width = right_boundaries[i] - left_boundaries[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
