class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                return i == n-1
            tmp = i + nums[i]
            nextI = i 
            for d in range(nums[i] + 1):
                j = i + d
                if j >= n-1:
                    return True
                if j + nums[j] > tmp:
                    tmp = j + nums[j]
                    nextI = j
            if i == nextI:
                return False
            i = nextI
        return True


        