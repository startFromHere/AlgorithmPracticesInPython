class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aMap = {}
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] in aMap:
                l = max(aMap[s[r]] + 1, l)
            aMap[s[r]] = r
            r += 1
            if r - l > ans:
                ans = r - l
        return ans