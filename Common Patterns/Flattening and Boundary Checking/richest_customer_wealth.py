"""
Time Complexity: O(M * N)
Space Complexity: O(1)
"""
# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts):
        maxwealth, wealth = 0, 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            maxwealth = max(maxwealth, wealth)
            wealth = 0
        return maxwealth