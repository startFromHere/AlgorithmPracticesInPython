class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, k
        n = len(nums)
        aSet = set()
        for r in range(n):
            if len(aSet) >= k+1:
                aSet.remove(nums[l])
                l += 1
            if nums[r] in aSet:
                return True
            aSet.add(nums[r])
        return False
        