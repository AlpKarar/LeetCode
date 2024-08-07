class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            cur_gas = gas[i]
            cur_i = i

            while cur_i < i + len(gas):
                cur_gas -= cost[cur_i % len(cost)]

                if cur_gas < 0:
                    break
                
                cur_gas += gas[(cur_i + 1) % len(gas)]
                cur_i += 1
            
            if cur_gas >= 0:
                return i
        
        return -1