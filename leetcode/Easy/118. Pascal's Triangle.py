"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        if numRows == 1:
            return [res[0]]
        elif numRows == 2:
            return res
        else:
            for i in range(2, numRows):
                res.append([1] + [res[-1][i]+res[-1][i+1] for i in range(len(res[-1])-1)] + [1])
            return res
                
        
