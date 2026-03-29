class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        max = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                count += 1
            else:
                count = 1
            if count > max:
                max = count
        return max