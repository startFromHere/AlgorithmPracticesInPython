class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        ans = 0
        while l < r:
            # ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                ans = max(ans, height[l] * (r-l))
                l += 1
            else:
                ans = max(ans, height[r] * (r-l))
                r -= 1
        return ans
        