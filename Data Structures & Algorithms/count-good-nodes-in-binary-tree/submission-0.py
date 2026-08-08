# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def f(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val>=maxVal else 0
            maxVal = max(node.val, maxVal)
            res += f(node.right, maxVal)
            res += f(node.left, maxVal)
            return res
        return f (root, root.val)
            