from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

        #We use Breadth-First Search (BFS) algorithm.

        if root is None:
            return []

        result = []
        current_level = [root] #The nodes we are handling.

        while current_level:
            result.append([node.val for node in current_level])

            next_level = [] #The nodes that will be handled in the next iteration.
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level

        return result