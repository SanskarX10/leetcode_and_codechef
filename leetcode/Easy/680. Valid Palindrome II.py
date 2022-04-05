"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""




class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        if s == s[::-1]:
            return True
        else:
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    x, y = s[l:r], s[l+1:r+1]
                    return x == x[::-1] or y == y[::-1]
            return False
            
            
                
        
