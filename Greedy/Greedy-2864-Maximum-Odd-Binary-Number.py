class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one_bit = 0

        for bit in s:
            if bit == "1":
                count_one_bit += 1
        
        return (count_one_bit - 1) * "1" + (len(s) - count_one_bit) * "0" + "1"