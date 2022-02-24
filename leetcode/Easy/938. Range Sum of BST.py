"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#ITERATIVE SOLUTION
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0
        
        while stack:
            curr = stack.pop()
            if curr:
                if curr.val >= low and curr.val <= high:
                    res += curr.val
                if curr.val > low:
                    stack.append(curr.left)
                if curr.val < high:
                    stack.append(curr.right)
        return res
            
            
        
        
