class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = [(i, score[i]) for i in range(len(score))]
        score_index_sorted = sorted(score_index, key = lambda x: x[1])[::-1]
        res = ["" for _ in range(len(score))]

        for i in range(len(score_index_sorted)):
            index, _ = score_index_sorted[i]
            
            if i == 0:
                res[index] = "Gold Medal"
            elif i == 1:
                res[index] = "Silver Medal"
            elif i == 2:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(i + 1)
        
        return res