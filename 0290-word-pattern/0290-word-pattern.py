class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False

        aMap = {}
        aMap1 = {}
        for i, c in enumerate(pattern):
            if c in aMap and aMap[c] != arr[i]:
                return False
            if arr[i] in aMap1 and aMap1[arr[i]] != c:
                return False
            aMap[c] = arr[i]
            aMap1[arr[i]] = c
        return True
                
