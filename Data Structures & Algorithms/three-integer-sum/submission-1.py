class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(1, len(nums) - 1):
            l, r = 0, len(nums) -1
            while l < i and r > i:
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                elif nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                else:
                    ret.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
        unique_lst = [list(t) for t in set(tuple(sublist) for sublist in ret)]
        return unique_lst