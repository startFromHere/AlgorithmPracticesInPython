class Solution:
    def intToRoman(self, num: int) -> str:
        aMap = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        keys = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        while num > 0:
            for key in keys:
                if num >= key:
                    num -= key
                    ans += aMap[key]
                    break
        return ans

        