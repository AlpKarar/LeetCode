class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = str(bin(num))[2:]
        sm = 2 ** len(num_bin) - 1
        
        return sm - num