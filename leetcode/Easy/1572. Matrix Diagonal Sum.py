"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        add = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    add += mat[i][j]
                if i+j == len(mat)-1:
                    add += mat[i][j]
        if len(mat)%2 != 0:
            add -= mat[len(mat)//2][len(mat)//2]
        return add
        
