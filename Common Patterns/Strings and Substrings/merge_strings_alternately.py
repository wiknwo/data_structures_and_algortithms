"""
Time Complexity: O(max(M, N))
Space Complexity: O(1)
M = len(word1), N = len(word2)
"""
# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Defining variables
        mergedstring, word1_index, word2_index = '', 0, 0
        # Iterating through both strings
        while word1_index < len(word1) and word2_index < len(word2):
            # Adding letters to merged string in alternating order
            mergedstring += word1[word1_index] + word2[word2_index]
            word1_index += 1
            word2_index += 1
        # Checking if there are still characters to merge for word1 in case it is longer than word2
        if word1_index < len(word1):
            mergedstring += word1[word1_index:]
        # Checking if there are still characters to merge for word2 in case it is longer than word1
        if word2_index < len(word2):
            mergedstring += word2[word2_index:]
        # Return the merged string
        return mergedstring    