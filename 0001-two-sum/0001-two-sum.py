class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i
        
        for i, num in enumerate(nums):
            key = target - num
            if key in dic:  # BigO(1)
                if i == dic[key]: continue
                else:
                    return [i, dic[key]]
                
        