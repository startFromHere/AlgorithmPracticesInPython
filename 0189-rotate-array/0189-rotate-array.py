class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # tmp = nums[-k:]+nums[:n-k]
        # for i in range(n):
        #     nums[i] = tmp[i]
        if k > 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]