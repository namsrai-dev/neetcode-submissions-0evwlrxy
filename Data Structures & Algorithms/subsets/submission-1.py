class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]

        for num in nums:
            new_arr = []
            for j in arr:  #  -> 1
                new_arr.append(j)
                arr2=j + [num]
                new_arr.append(arr2)
            
            arr = new_arr
        return arr
