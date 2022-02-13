"""Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column."""

 






class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = {min(r) for r in matrix}
        max_col = {max(c) for c in zip(*matrix)}
        return list(min_row & max_col)
        
