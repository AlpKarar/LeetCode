class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sorted_s = ""
        isFirst = True

        for bit in s:
            if bit == "1":
                if isFirst:
                    isFirst = False
                else:
                    sorted_s = bit + sorted_s
            else:
                sorted_s += bit
        
        if not isFirst:
            sorted_s += "1"
        
        return sorted_s