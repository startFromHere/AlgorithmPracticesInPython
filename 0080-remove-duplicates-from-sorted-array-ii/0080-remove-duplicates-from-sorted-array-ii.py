class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j, n = 1, len(nums)
        for i in range(1, n):
            if j == 1 or nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
        return j