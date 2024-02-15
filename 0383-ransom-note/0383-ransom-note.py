from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b = Counter(magazine)
        for k, v in Counter(ransomNote).items():
            # print(k, v)
            if k not in b:
                return False
            if b[k] < v:
                return False
        return True