class Solution:
    def reverse(self, x: int) -> int:
        a = self.myReverse(x)
        if a > (1 << 31) - 1:
            return 0
        if a < - (1 << 31):
            return 0
        return a

    def myReverse(self, x: int) -> int:
        if x < 0:
            return -self.myReverse(-x)
        n = x
        r = 0
        while n > 0:
            tmp = n % 10
            r = r * 10 + tmp
            n = n // 10
        return r
        
        