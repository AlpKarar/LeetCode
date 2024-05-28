class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:        
        max_index_garbage = dict()

        for i in range(len(garbage) - 1, -1, -1):
            if "P" not in max_index_garbage:
                if garbage[i].count("P") > 0:
                    max_index_garbage["P"] = i
            
            if "M" not in max_index_garbage:
                if garbage[i].count("M") > 0:
                    max_index_garbage["M"] = i
            
            if "G" not in max_index_garbage:
                if garbage[i].count("G") > 0:
                    max_index_garbage["G"] = i

        res = 0

        for g in max_index_garbage:
            res += sum(travel[:max_index_garbage[g]])
        
        
        for i in range(len(garbage)):
            num_p = garbage[i].count("P")
            num_g = garbage[i].count("G")
            num_m = garbage[i].count("M")

            res += num_p + num_g + num_m
        
        return res