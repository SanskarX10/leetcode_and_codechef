"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q, curr = [root], 0
        
        while len(q):
            qlen, ans = len(q), 0
            
            for i in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                
                if curr.left :
                    q.append(curr.left)
                if curr.right : 
                    q.append(curr.right)
        return ans
            
