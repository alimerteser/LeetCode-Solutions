from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        #Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        #We use Depth First Search (DFS) algorithm.

        isSame = True #We generate a global variable to check if the trees are the same or not.

        def dfs(p, q):
            nonlocal isSame

            if isSame == False: #If two equivalent nodes are not the same, there is no need to check the other nodes.
                return

            if (p and not q) or (not p and q): #We check if one is None and the other is not.
                isSame = False
                return

            if p and q:
                if p.val != q.val:
                    isSame = False
                    return
                dfs(p.left, q.left)
                dfs(p.right, q.right)

        dfs(p, q)
        return isSame
