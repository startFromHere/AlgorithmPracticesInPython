class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1.0
        while abs(ans - x / ans) > 0.0000001:
            ans = (ans + x / ans) / 2
        return int(ans)
        