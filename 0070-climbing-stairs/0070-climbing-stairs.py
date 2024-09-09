class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            tmp = a
            a = b
            b = tmp + a
        return b
        