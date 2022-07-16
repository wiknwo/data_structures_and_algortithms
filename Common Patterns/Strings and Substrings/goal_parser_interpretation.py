"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
# https://leetcode.com/problems/goal-parser-interpretation/
class Solution:
    def interpret(self, command: str) -> str:
        # Defining variables
        alphabet = {'G': 'G', '()': 'o', '(al)': 'al'}
        interpretation = ''
        index = 0
        # Iterating through command
        while index < len(command):
            # Parsing command
            if command[index] == 'G':
                interpretation += alphabet[command[index]]
                index += 1
            elif command[index:index + 2] == '()':
                interpretation += alphabet[command[index:index + 2]]
                index += 2
            elif command[index:index + 4] == '(al)':
                interpretation += alphabet[command[index: index + 4]]
                index += 4
        # Return Goal Parser's interpretation of command
        return interpretation