from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        ans = 0
        for k, v in Counter(s).items():
            if v%2:
                odd = True
                if v > 1:
                    ans += (v-1)
            else:
                ans += v
            
        if odd:
            ans += 1
            
        return ans
                
        
        