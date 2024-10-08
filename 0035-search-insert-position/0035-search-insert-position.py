class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return l
