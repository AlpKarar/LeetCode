class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ref = customers[0][0]
        total_waiting_time = 0
        num_customers = 0

        for customer in customers:
            if ref > customer[0]:
                total_waiting_time += ref - customer[0] + customer[1]
            else:
                if ref < customer[0]:
                    ref = customer[0]
                
                total_waiting_time += customer[1]
            
            ref += customer[1]
            num_customers += 1
        
        return total_waiting_time / num_customers