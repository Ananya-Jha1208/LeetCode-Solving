class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''.join(a for a in s if a.isalnum()).lower()
        return ans[::-1] == ans
        
