from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
        
        for i in t:
            dic[i] -= 1
        
        
        if any(value !=0 for value in dic.values()):
            return False
        return True
            
            
        