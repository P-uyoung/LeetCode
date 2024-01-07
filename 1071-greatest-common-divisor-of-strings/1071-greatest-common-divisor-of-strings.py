import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = len(str1), len(str2)
        c = math.gcd(a, b)
        divisors = set()
        for i in range(1, int(math.sqrt(c)) + 1):
            if c % i== 0:
                divisors.add(i)
                divisors.add(c//i)
        divisors = sorted(divisors, reverse=True)
        
        for i in divisors:
            q1, r1 = divmod(a, i)
            q2, r2 = divmod(b, i)
            if r1 != 0 or r2 != 0:
                continue
            patt = str1[:i]
            yes = True
            for j in range(i, a+1, i):
                if patt != str1[j-i:j]:
                    yes = False
                    break
            if yes:
                for j in range(i, b+1, i):
                    if patt != str2[j-i:j]:
                        yes = False
                        break
            if yes:
                return patt
        return ''
                    
                
                
            
            
            
            
        