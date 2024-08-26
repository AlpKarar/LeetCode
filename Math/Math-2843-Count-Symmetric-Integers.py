class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if high < 10:
            return 0
        
        if low < 10:
            low = 10
        
        res = 0

        for num in range(low, high + 1):
            temp = num
            sum_arr = [0]
            i = 0

            while temp > 0:
                digit = temp % 10
                sum_arr.append(sum_arr[-1] + digit)
                temp //= 10
                i += 1
            
            sum_arr = sum_arr[1:]
            isEven = i % 2 == 0

            if isEven and sum_arr[i // 2 - 1] == sum_arr[-1] - sum_arr[i // 2 - 1]:
                res += 1
        
        return res