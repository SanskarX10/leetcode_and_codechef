"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res, min_d = [], float('inf')

        for i in range(len(arr)-1):
            if min_d >= arr[i+1] - arr[i]:
                if min_d > arr[i+1] - arr[i]:
                    res = [] # res.clear()
                    min_d = arr[i+1] - arr[i]
                res.append([arr[i], arr[i+1]])
        return res
