class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        ans = ""
        s0 = strs[0]
        for i in range(len(s0)):
            tmp = s0[i]
            for s in strs[1:]:
                if s[i] != tmp:
                    return ans
            ans += tmp
        return ans
                
        