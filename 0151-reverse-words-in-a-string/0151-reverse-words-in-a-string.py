class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        for i in s.split(' ')[::-1]:
            if i != '':
                ans += ' '
                ans += i
                
        return ans[1:]
        