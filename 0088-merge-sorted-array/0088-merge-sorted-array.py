class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            if nums1[i] > nums2[j] or i - j == m:
                nums1[i+1:] = nums1[i:m+n-1]
                nums1[i] = nums2[j]
                j += 1
            i += 1
        

        