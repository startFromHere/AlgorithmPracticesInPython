class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, n = 0, len(nums)
        for i in range(n):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j+1