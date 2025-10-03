class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                x = stack.pop()
                res[x] = i-x
            stack.append(i)

        return res
