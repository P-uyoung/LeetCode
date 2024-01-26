from collections import defaultdict 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        l = len(nums)
        for n in nums:
            if counts[n] > l//2:
                return n
            counts[n] += 1
        
        return max(counts, key=counts.get)
        