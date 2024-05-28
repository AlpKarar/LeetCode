class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0

        for row in bank:
            numOfOnes = row.count("1")

            if numOfOnes > 0:
                res += prev * numOfOnes
                prev = numOfOnes
        
        return res