class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1, s2 = list(reversed(a)), list(reversed(b))
        m, n = len(s1), len(s2)
        if m > n:
            s1, s2 = s2, s1
        for i in range(abs(m - n)):
            s1.append("0")
        res = ""
        carry = 0
        i = 0
        while i < len(s1):
            num = int(s1[i]) + int(s2[i]) + carry
            if num >= 2:
                carry = 1
            else:
                carry = 0
            res += str(num%2)
            i += 1
        if carry == 1:
            res += '1'
        return res[::-1]

        
