# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# 思路: 因为w的长度为10^4，w[i]的大小为10^5，所以对每个数生成相应个数的实例会爆内存.
# 考虑生成长度为w.length的累计weight数组，然后从1到总sum_weight之间抽取一个数，查找该数落在的范围(二分查找第一个比它大的数)，作为pick出的index

import random
class Solution:

    def __init__(self, w):
        self.sumW=[0]*len(w)
        curS=0
        for i in range(len(w)):
            curS+=w[i]
            self.sumW[i]=curS
        self.totalW=curS

    def pickIndex(self):
        w=random.randint(1,self.totalW)
        return self.binary_search(w)

    def binary_search(self,w):
        l,r=0,len(self.sumW)-1
        while l<r:
            mid=l+(r-l)//2
            if self.sumW[mid]==w:
                return mid
            elif self.sumW[mid]<w:
                l=mid+1
            else:
                r=mid
        return l

a=Solution([1,3])
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())