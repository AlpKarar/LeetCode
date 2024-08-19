class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks = sorted(tasks)
        processorTime = sorted(processorTime)[::-1]
        num_processors = len(processorTime)
        r = len(tasks) // num_processors
        max_tasks = []

        for i in range(1, num_processors + 1):
            max_tasks.append(tasks[i * r - 1])
        
        res = 0

        for i in range(len(processorTime)):
            res = max(res, processorTime[i] + max_tasks[i])
        
        return res