class Solution:
    def canCompleteCircuit(self, gas, cost):
        # three points:
        # 1. 只要总gas大于总cost, 一定有解
        # 2. 如果有解, 这个解一定是从第一个能走到末尾的index开始,因为如果解为后面的index, 那么第一个index也成为解
        # 3. 如果在某一点cur_gas<0,, 那么一定不能从其前面的index开始, 因为从前面的开始会截掉一段gas大于0的路,只会让cur_gas更小,到当前index也会小于0
        start,cur_gas,total_gas=0,0,0
        for i in range(len(gas)):
            cur_gas+=gas[i]-cost[i]
            total_gas+=gas[i]-cost[i]
            if cur_gas<0:
                start,cur_gas=i+1,0
        return start if total_gas>=0 else -1

a=Solution()
print(a.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(a.canCompleteCircuit([2,3,4],[3,4,3]))
print(a.canCompleteCircuit([3,1,1],[1,2,2]))