class Solution:
    def longestConsecutive(self, nums: list) -> int:
        count = 0
        increase = []
        decrease = []
        
        nums = list(set(nums))
        nums.sort()
        
        for v in nums:
            if not increase or v-increase[-1] == 1:
                increase.append(v)
            
            else:
                count = max(count,len(increase))
                increase = [v]
            
            if not decrease or decrease[-1]-v == 1:
                decrease.append(v)
                
            else:
                count = max(count,len(decrease))
                decrease = [v]
              
        if increase and count < len(increase):
            count = len(increase)
        if decrease and count < len(decrease):
            count = len(decrease)
        return count 