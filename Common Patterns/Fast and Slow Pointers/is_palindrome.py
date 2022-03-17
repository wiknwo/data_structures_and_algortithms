"""
Program to check whether a linked list is a Palindrome
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        """
        1. Find the midpoint of the linked list
        2. Reverse the linked list from the midpoint
        3. Compare unreversed half of linked list with reversed half of linked list and check if they are equal
        """
        if head is None or head.next is None:
            return True
        
        unreversed_half = head
        midpoint = self.midpoint(head)
        reversed_half = self.reverse(midpoint)
        while reversed_half != None:
            if unreversed_half.val != reversed_half.val:
                return False
            unreversed_half = unreversed_half.next
            reversed_half = reversed_half.next
        return True
        
        
    def reverse(self, head):
        previous, current = None, head
        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        return previous
    
    def midpoint(self, head):
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer