class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        sum_count = nums[0]
        ans = inf
        while r <= len(nums) - 1:
            if sum_count < target:
                r += 1
                if r <= len(nums) - 1:
                    sum_count += nums[r]
            else:
                ans = min(ans, r - l + 1)
                sum_count -= nums[l]
                l += 1
        if ans == inf:
            return 0
        return ans
        