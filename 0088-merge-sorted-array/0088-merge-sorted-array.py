class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while i < m + n and j < n:
            if nums1[i] == 0 and i >= m+j:
                nums1[i] = nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                nums1[i:] = [nums2[j]] + nums1[i:-1]
                j += 1
            i += 1