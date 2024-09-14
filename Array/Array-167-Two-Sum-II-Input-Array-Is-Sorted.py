class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        res = [0, 0]

        while l < r:
            if numbers[l] + numbers[r] == target:
                res[0] = l + 1
                res[1] = r + 1
                break
            
            if numbers[l] + numbers[r] > target:
                 r -= 1
            else:
                l += 1
        
        return res