class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2

        for num in range(n, -1, -1):
            left_sum = num * (num + 1) // 2
            right_sum = total - left_sum + num

            if left_sum == right_sum:
                return num
        
        return -1