class Solution:
    def isValid(self, s: str) -> bool:
        aMap = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        t = []
        for c in s:
            if c in aMap:
                if not t or t[-1] != aMap[c]:
                    return False
                else:
                    t.pop()
            else:
                t.append(c)
        return not t

        