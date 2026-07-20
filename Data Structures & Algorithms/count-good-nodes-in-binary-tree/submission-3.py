# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxtillNow):
            if not node:
                return 0
            good = 1 if node.val >= maxtillNow else 0
            maxtillNow = max(node.val, maxtillNow)
            return good + dfs(node.left, maxtillNow) + dfs(node.right, maxtillNow)
        return dfs(root, root.val)
            