"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        elements = []
        
        if not root:
            return elements
        
        if root.left:
            elements += self.postorderTraversal(root.left)

        if root.right:
            elements += self.postorderTraversal(root.right)
            
        elements.append(root.val)
    
        return elements
        
        
         
