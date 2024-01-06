class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        k = min(len1, len2)
        ans = ''
        for a, b in zip(word1, word2):
            ans += a
            ans += b
        if len1 > k:
            ans += word1[k:]
        elif len2 > k:
            ans += word2[k:]
        return ans
        


        