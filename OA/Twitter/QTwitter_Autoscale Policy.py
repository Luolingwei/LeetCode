
# 对每个point进行范围判断, 跳过10个point加11

from math import ceil
class Solution:
    def Autoscale(self,start,avgUtils):
        curS=start
        i,L=0,len(avgUtils)
        while i<L:
            if avgUtils[i]<25 and curS>1:
                curS=ceil(curS/2)
                i+=11
            elif avgUtils[i]>60:
                curS*=2
                i+=11
            else:
                i+=1
        return curS

a=Solution()
print(a.Autoscale(1,[5,10,80]))
print(a.Autoscale(2,[25,23,1,2,3,4,5,6,7,8,9,10,76,80]))