num_dicts = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        ret = []

        def backtrack(num_dict):
            nonlocal ret
            if len(ret) == 0:
                ret = num_dict
                return
            
            my_arr = []
            # ret_copy = ret.copy()
            for i in ret:
                for j in num_dict:
                    my_arr.append(i+j)
                  
            ret = my_arr

        
        for i in digits:
            backtrack(num_dicts[i])

        return ret
