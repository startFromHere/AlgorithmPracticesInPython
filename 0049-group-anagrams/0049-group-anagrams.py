class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = defaultdict(list)
        ans = []
        for s in strs:
            key = str(sorted(s))
            aMap[key].append(s)
        return aMap.values()

        