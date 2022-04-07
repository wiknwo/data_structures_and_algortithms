# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps, lpslength = '', 0
        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lpslength:
                    lps = s[l:r + 1]
                    lpslength = (r - l + 1)
                l -= 1
                r += 1
            
            # Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lpslength:
                    lps = s[l:r + 1]
                    lpslength = (r - l + 1)
                l -= 1
                r += 1
        return lps