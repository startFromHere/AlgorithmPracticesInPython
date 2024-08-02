class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > n // 2:
                return num
        return 0

        