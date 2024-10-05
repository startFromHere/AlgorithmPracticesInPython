class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            aMap[key].append(s)
        ans = []
        for key in aMap:
            ans.append(aMap[key])
        return ans

        