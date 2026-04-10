class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def arr_sum(my_arr):
            total_sum = 0
            for i in my_arr:
                total_sum += i
            return total_sum

        def dfs(arr1, arr2):
            print()
            if arr_sum(arr2) == target:
                ret.append(arr2)
                # return
            
            for i, num in enumerate(arr1):
                new_arr = arr2.copy()
                new_arr.append(num)
                if arr_sum(new_arr) <= target:
                    dfs(arr1[i:], new_arr)

        for i, num in enumerate(nums):
            dfs(nums[i:], [num])
            # print(i, num)

        return ret
