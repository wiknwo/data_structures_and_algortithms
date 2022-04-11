# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            # If nums[i] != 0
            if nums[i]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1