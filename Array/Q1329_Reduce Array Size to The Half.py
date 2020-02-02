import collections
import math

# 思路: 先Counter统计，从大到小统计数量，直到超过一半

class Solution:
    def minSetSize(self, arr):
        count=collections.Counter(arr)
        target,curn,res=math.ceil(len(arr)/2),0,0
        for n in sorted(count.values(),reverse=True):
            curn+=n
            res+=1
            if curn>=target: return res