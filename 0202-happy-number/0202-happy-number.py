class Solution:
    def isHappy(self, n: int) -> bool:
        aMap = set()
        
        while n != 1:
            tmp = 0
            while n > 0:
                tmp += (n % 10) * (n % 10)
                n //= 10
            if tmp in aMap:
                return False
            aMap.add(tmp)
            n = tmp
        
        return True
        