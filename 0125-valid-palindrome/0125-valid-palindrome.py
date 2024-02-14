class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        for i in s:
            if i.isalnum():
                ans += i
 
        if ans.lower() == ans[::-1].lower():
            return True
        return False
                
        