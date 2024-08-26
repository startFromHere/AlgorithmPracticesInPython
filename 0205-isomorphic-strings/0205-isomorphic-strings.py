class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        aMap = {}
        aMap1 = {}
        for i, c in enumerate(s):
            if c in aMap and aMap[c] != t[i]:
                return False
            if t[i] in aMap1 and aMap1[t[i]] != c:
                return False
            aMap[c] = t[i]
            aMap1[t[i]] = c
        return True

        