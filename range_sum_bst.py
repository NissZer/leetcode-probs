# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.res += node.val
                if node.val < R:
                    dfs(node.right)
                if node.val > L:
                    dfs(node.left)
        
        dfs(root)
        return self.res