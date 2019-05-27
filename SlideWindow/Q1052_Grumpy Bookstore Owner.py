
# 思路: 移动窗口，寻找X长度的窗口能带来的最大的顾客数的提升.然后用本底数值加上maxGap即可.

class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        left,gap,maxGap=0,0,0
        for i in range(len(grumpy)):
            gap+=customers[i]*grumpy[i]
            if i-left>=X:
                gap,left=gap-customers[left]*grumpy[left],left+1
            maxGap=max(maxGap,gap)
        return sum([customers[i]*abs(grumpy[i]-1) for i in range(len(customers))])+maxGap

a=Solution()
print(a.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
print(a.maxSatisfied([1,5,1,2],[0,1,1,1],3))
