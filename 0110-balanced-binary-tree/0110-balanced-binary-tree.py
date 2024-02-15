# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root) -> int:
        if not root:
            return 0
        leftValue = self.recursive(root.left)
        rightValue = self.recursive(root.right)
        
        
        if leftValue == -1 or rightValue == -1:
            return -1 
        
        if abs(leftValue-rightValue) > 1:
            return -1
        
        return max(leftValue, rightValue) + 1
        
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.recursive(root) == -1:
            return False
        return True
            
        
        