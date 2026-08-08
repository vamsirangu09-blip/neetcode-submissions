# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = []
        q = deque([root])
        
        while q:
            k=[]
            for i in range(len(q)):
                node=q.popleft()
                k.append(node.val)
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            level.append(k)
        return level