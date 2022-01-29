"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = (y ^ x)
        return str(format(res, "b")).count("1")
        
