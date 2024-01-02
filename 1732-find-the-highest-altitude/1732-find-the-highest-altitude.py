class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        prev = 0
        for g in gain:
            prev += g
            highest = max(highest, prev)
        
        return highest
            
        