class Solution:
    def reverseVowels(self, s: str) -> str:
        index = []
        vowel = []
        for i,k in enumerate(s):
            if k in ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']:
                index.append(i)
                vowel.append(k)
        s = list(s)
        for i, v in zip(index,vowel[::-1]):
            s[i] = v
        return ''.join(s)
            
        