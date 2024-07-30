class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        while r < n:
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
            r += 1
        return l+1