"""
Time Complexity: O(N^2)
Space Complexity: O(N)
"""
# https://stackoverflow.com/questions/71832544/i-want-to-know-this-functions-time-complexity-and-space-complexity
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
class Solution:
    def sumOddLengthSubarrays(self, arr):
        odd_subsequences = []
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr)):
                if j + i <= len(arr):
                    odd_subsequences.append(arr[j:j + i])
        return sum(sum(subsequence) for subsequence in odd_subsequences) 
        