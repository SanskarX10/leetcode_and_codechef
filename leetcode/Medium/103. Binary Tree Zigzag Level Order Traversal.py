"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
"""




class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = collections.deque()
        lev_count = 0        
        q.append(root)
            
        while q:             
            qlen = len(q)
            level = []               
            for i in range(qlen):
                curr = q.popleft()                  
                if curr:
                    level.append(curr.val) 
                    q.append(curr.left)
                    q.append(curr.right)
            lev_count += 1
                
            if level :
                if lev_count % 2 == 0:
                    res.append(level[::-1])
                else:
                    res.append(level)
            
        return res
