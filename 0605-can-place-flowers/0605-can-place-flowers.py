class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = False
        for k in flowerbed:
            if k == 0:
                if not prev:
                    n -= 1
                    prev = True
                else:
                    prev = False
            else:
                if prev:
                    n += 1
                prev = True
                
        return n <= 0
                    
                    
                    
                    
            
        