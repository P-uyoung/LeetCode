class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '[', '{']
        close = [')', ']', '}']
        if len(s)%2 == 1:
            return False
        if s[0] in close:
            return False
        
        new = []
        for i in range(1,len(s)+1):
            char = s[-i]
            if char in close:
                new.append(char)
            else:
                idx = open.index(char)
                if new == []: return False
                if idx != close.index(new.pop()): return False
        if new != []:
            return False
        else: 
            return True