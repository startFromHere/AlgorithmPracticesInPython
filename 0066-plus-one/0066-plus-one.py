class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits
        n = len(digits)
        i = n-1
        while ans[i] == 9:
            ans[i] = 0
            i -= 1
            if i < 0:
                return [1] + ans
        ans[i] += 1
        return ans