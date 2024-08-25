class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1, cnt2 = Counter(), Counter()
        for c in ransomNote:
            cnt1[c] += 1
        for c in magazine:
            cnt2[c] += 1
        for key in cnt1.keys():
            if key not in cnt2 or cnt2[key] < cnt1[key]:
                return False
        return True

        