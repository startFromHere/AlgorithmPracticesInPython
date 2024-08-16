class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        remained_gas = 0
        index = 0
        for i in range(len(gas)):
            remained_gas += gas[i] - cost[i]
            if remained_gas < 0:
                remained_gas = 0
                index = i + 1
        return index