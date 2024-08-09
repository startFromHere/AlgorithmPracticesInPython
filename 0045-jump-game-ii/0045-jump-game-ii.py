class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        cnt = 0
        if n <= 1:
            return 0
        while i < n:
            tmp = i
            nextI = i
            
            for j in range(nums[i]+1):
                if i + j >= n-1:
                    return cnt + 1
                if i + j + nums[i+j] > tmp:
                    tmp = i + j + nums[i+j]
                    nextI = i + j
            cnt += 1
            i = nextI
        return cnt
        
                
