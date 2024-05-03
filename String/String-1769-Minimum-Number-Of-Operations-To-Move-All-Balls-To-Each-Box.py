class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        numberOfPreviousOnes = int(boxes[0])

        for i in range(1, n):
            left[i] = left[i - 1] + numberOfPreviousOnes

            if boxes[i] == "1":
                numberOfPreviousOnes += 1
        
        numberOfPreviousOnes = int(boxes[-1])

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + numberOfPreviousOnes

            if boxes[i] == "1":
                numberOfPreviousOnes += 1
        
        return [left[i] + right[i] for i in range(n)]