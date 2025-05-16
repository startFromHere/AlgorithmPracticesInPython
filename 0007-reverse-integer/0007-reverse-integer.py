class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        n = x
        r = 0
        while n > 0:
            tmp = n % 10
            r = r * 10 + tmp
            n = n // 10
        r = flag * r
        if r < (-1 << 31):
            return 0
        if r > (1 << 31) - 1:
            return 0
        return r
        
        