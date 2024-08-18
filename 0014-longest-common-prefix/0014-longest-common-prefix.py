class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for s in strs:
                if len(s) <= i or s[i] != tmp:
                    return ans
            ans += tmp
        return ans
                
        