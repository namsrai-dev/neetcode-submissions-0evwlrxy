class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i != len(nums) - 1:
                 if num == nums[i+1]:
                    return num