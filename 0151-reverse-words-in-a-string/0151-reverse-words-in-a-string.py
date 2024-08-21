class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list([x for x in s.split() if len(x) > 0])
        arr.reverse()
        return " ".join(arr)
        