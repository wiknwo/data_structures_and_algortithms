# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val):
        left, right, swaps = 0, len(nums) - 1, 0
        while left <= right:
            if nums[right] == val:
                right -= 1
                swaps += 1
            elif nums[left] != val:
                left += 1
            elif nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                swaps += 1
        return len(nums) - swaps