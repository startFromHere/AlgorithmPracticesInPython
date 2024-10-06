class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        l, r = 0, 0
        
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        while r < n:
            if nums[r] - nums[l] == r-l:
                ans = max(ans, r-l + 1)
            else:
                l = r
            r += 1
        return ans
        