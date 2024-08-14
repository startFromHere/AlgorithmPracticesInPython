class Solution:
    def romanToInt(self, s: str) -> int:
        aDic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        aDic1 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if i+1 < n and s[i:i+2] in aDic1:
                ans += aDic1[s[i:i+2]]
                i += 2
            else:
                ans += aDic[s[i: i+1]]
                i += 1
        return ans

        