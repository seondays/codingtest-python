# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        if not (root.left or root.right):
            return root

        else:
            tem = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(tem)
        
        return root