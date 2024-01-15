class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        inters = nums1 & nums2
        return [list(nums1-inters), list(nums2-inters)]
        