"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()
        q.append(root)
        res = []
        
        while q:  
            qlen = len(q)
            level = []              
            for i in range(qlen):
                curr = q.popleft()
                
                if curr:      
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                    
            if level:
                res.append(level)
        
        return res[::-1]
