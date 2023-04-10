class Solution:
    def longestConsecutive(self, nums: list) -> int:
        longest = 0
        num_dic = {}
        for v in nums:
            num_dic[v] = True
        
        for v in nums:
            prev = v-1
            next = v+1
            if prev not in num_dic:
                count = 1
                while next in num_dic:
                    count += 1
                    next += 1
                longest = max(longest, count)
        return longest