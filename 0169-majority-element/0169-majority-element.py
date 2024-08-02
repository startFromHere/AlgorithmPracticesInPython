class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter()
        n = len(nums)
        h = n // 2
        for i in range(h+1):
            cnt[nums[i]] += 1
        for i in range(h+1, n):
            cnt[nums[i]] += 1
            if  cnt[nums[i]] > h:
                return nums[i]
        return nums[0]

        