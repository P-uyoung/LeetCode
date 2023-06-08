from itertools import combinations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_loca = list(combinations([i-1 for i in range(2*n)], n))
        output = []
        
        for idxs in open_loca:
            arr = [1 if i in idxs else -1 for i in range(2*n)]
            sum, i = 0, 0
            while i < 2*n:
                if sum < 0:
                    break
                sum += arr[i]
                i += 1
            
            if i == 2*n:
                output.append("".join(["(" if x == 1 else ")" for x in arr]))
                
        return output
                
                
        
                
                
                        