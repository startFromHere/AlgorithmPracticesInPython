class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        i = 1
        while n > 0:
            if n & i > 0:
                cnt += 1
                n -= i
            i *= 2
        return cnt