class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def mergeSort(arr, start, end):
            if start >= end:
                return

            m = start + (end - start) // 2
            mergeSort(arr, start, m)
            mergeSort(arr, m + 1, end)
            
            sort(arr, start, m, end)
        
        def sort(arr, s, m, e):
            leftSubLength = m - s + 1
            rightSubLength = e - m

            leftSub = [0] * leftSubLength
            rightSub = [0] * rightSubLength

            for i in range(leftSubLength):
                leftSub[i] = arr[s + i]
            
            for i in range(rightSubLength):
                rightSub[i] = arr[m + 1 + i]
            
            leftIndex = 0
            rightIndex = 0
            curIndex = s

            while leftIndex < leftSubLength and rightIndex < rightSubLength:
                if leftSub[leftIndex] > rightSub[rightIndex]:
                    arr[curIndex] = rightSub[rightIndex]
                    rightIndex += 1
                else:
                    arr[curIndex] = leftSub[leftIndex]
                    leftIndex += 1
                
                curIndex += 1
            
            while leftIndex < leftSubLength:
                arr[curIndex] = leftSub[leftIndex]
                leftIndex += 1
                curIndex += 1
            
            while rightIndex < rightSubLength:
                arr[curIndex] = rightSub[rightIndex]
                rightIndex += 1
                curIndex += 1
        
        mergeSort(nums, 0, len(nums) - 1)