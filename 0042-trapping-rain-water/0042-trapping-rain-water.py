class Solution:
    def trap(self, height: List[int]) -> int:
        ltr, rtl = [], []
        n = len(height)
        maxl, maxr = height[0], height[-1] 
        for i in range(n):
            maxl = max(maxl, height[i])
            maxr = max(maxr, height[-i-1])
            ltr.append(maxl)
            rtl.append(maxr)
        rtl.reverse()
        ans = 0
        for i in range(i):
            ans += (min(ltr[i], rtl[i]) - height[i])
        return ans

        