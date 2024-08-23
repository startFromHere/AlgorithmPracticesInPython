class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for i in range(numRows)]
        flag = True
        i = 0
        for c in s:
            arr[i].append(c)
            i += (1 if flag else -1)
            if i == numRows:
                flag = not flag
                i = max(0, i - 2)
            if i < 0:
                flag = not flag
                i = min(i + 2, numRows - 1)
        ans = ""
        for subArr in arr:
            ans += ''.join(subArr)
        
        return ans



        