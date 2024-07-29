class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for i in range(n):
            smaller_in_left = 0
            greater_in_left = 0
            smaller_in_right = 0
            greater_in_right = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    smaller_in_left += 1
                elif rating[j] > rating[i]:
                    greater_in_left += 1
            
            for k in range(i + 1, n):
                if rating[k] < rating[i]:
                    smaller_in_right += 1
                elif rating[k] > rating[i]:
                    greater_in_right += 1
        
            res += smaller_in_right * greater_in_left + greater_in_right * smaller_in_left

        return res