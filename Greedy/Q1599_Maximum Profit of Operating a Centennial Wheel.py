
# 思路: 每次来一定数量的游客, 最多处理4人，动态记录剩下的游客人数以及profit即可

class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        left,curp,maxp,count = 0,0,float('-inf'),0
        res,i = 0,0
        while left>0 or i<len(customers):
            count += 1
            if i<len(customers): left += customers[i]
            curp += min(4,left)*boardingCost - runningCost
            if curp>maxp:
                maxp = curp
                res = count
            left -= min(4,left)
            i+=1
        return res if maxp>0 else -1


a=Solution()
print(a.minOperationsMaxProfit([8,3],5,6))
print(a.minOperationsMaxProfit([10,9,6],6,4))