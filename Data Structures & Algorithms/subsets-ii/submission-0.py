class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = [[]]

        for num in nums:
            arr = []
            for i in ret:
                # print("the i was", i)
                arr.append(i)
                
                i_cop = i.copy()
                i_cop.append(num)
                if i_cop not in ret:
                    arr.append(i_cop)

            ret = arr

        return ret