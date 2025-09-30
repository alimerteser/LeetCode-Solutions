from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for num in i:
                if ord(num) >= ord("1") and ord(num) <= ord("9"):
                    if num in seen:
                        return False
                    else:
                        seen.add(num)

        for i in range(len(board[0])):  # column
            seen = set()
            for j in range(len(board)):  # row
                if ord(board[j][i]) >= ord("1") and ord(board[j][i]) <= ord("9"):
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])

        squares = {f"sqr{i // 3}{j // 3}": [] for i in range(len(board[0])) for j in range(len(board))}
        for i in range(len(board[0])):
            for j in range(len(board)):
                sqr = "sqr" + str(i // 3) + str(j // 3)
                squares[sqr].append(board[i][j])

        for i in squares.values():
            seen = set()
            for num in i:
                if ord(num) >= ord("1") and ord(num) <= ord("9"):
                    if num in seen:
                        return False
                    else:
                        seen.add(num)

        return True