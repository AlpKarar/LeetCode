class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        visited = dict()

        for i in range(len(nums)):
            if nums[i] < i:
                visited[i] = nums[i]
                nums[i] = visited[nums[i]]
                visited.pop(nums[i], None)
            elif nums[i] > i:
                visited[i] = nums[i]
                nums[i] = nums[nums[i]]
        
        return