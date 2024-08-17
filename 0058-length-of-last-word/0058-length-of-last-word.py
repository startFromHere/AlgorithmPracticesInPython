class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        tmp = 0
        for c in s:
            if c == " ":
                tmp = 0
            else:
                tmp += 1
                ans = tmp

        return ans


        