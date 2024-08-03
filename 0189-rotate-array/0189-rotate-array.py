class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # for i in range(k):
        #     last = nums[-1]
        #     nums[1:] = nums[:-1]
        #     nums[0] = last
        tmp = nums[-k:]+nums[:n-k]
        for i in range(n):
            nums[i] = tmp[i]
        