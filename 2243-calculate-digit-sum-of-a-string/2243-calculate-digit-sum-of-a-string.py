class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            new_s = ''
            for i in range(0,n,k):
                tmp = 0
                for j in range(i,i+k):
                    if j < n:
                        tmp += int(s[j])
                new_s += str(tmp)
            
            s = new_s
            n = len(s)
        
        return s
