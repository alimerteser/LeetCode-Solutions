class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(path, open, close):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open >= close:
                if open < n:
                    path.append('(')
                    backtrack(path, open + 1, close)
                    path.pop()
                if close < n:
                    path.append(')')
                    backtrack(path, open, close + 1)
                    path.pop()


        backtrack([], 0, 0)
        return res
