class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, k
        n = len(nums)
        aMap = {}
        for i in range(min(k+1, n)):
            print("i:", i)
            if nums[i] in aMap:
                return True
            aMap[nums[i]] = i
            
        i = k+1
        while i < n:
            key = nums[i-k-1]
            aMap.pop(key)
            if nums[i] in aMap:
                return True
            aMap[nums[i]] = i
            print("dict:", dict)
            i += 1
        return False

        