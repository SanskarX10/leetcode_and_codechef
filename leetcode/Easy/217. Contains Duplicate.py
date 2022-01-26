"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
        return True if count>0 else False
