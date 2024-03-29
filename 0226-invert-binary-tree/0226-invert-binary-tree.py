# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recursive(node):
            if not node:
                return 
            
            node.left, node.right = node.right, node.left
            if node.left:
                recursive(node.left)
            if node.right:
                recursive(node.right)
        
        
        recursive(root)
        return root