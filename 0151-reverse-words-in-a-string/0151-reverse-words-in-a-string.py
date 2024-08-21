class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([x for x in s.split() if len(x) > 0]))
        