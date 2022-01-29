"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""




class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                res.append(nums[i])
        return res
        
        
