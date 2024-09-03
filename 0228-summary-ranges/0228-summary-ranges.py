class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        l, r = nums[0], nums[0]-1
        ans = []
        for n in nums:
            if n == r + 1:
                r = n
            else:
                ans.append(str(l) if l == r else str(l)+"->"+str(r))
                l, r = n, n
        ans.append(str(l) if l == r else str(l)+"->"+str(r))
        return ans
                 

        