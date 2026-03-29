class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_dict = set(nums)
        if len(new_dict) == len(nums):
            return False
        return True