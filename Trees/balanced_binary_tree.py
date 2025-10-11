from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Given a binary tree, determine if it is height-balanced.
        #A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

        #We use Depth First Search (DFS) algorithm.

        isBalanced = True #We use a global variable so that we can check the tree is balanced or not.

        def dfs(root: Optional[TreeNode]):
            if root is None: return 0

            nonlocal isBalanced
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1:
                isBalanced = False

            return 1 + max(left_height, right_height)

        dfs(root)
        return isBalanced
