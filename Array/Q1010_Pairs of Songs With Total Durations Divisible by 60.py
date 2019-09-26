
# 思路: 都除以60, 然后在counter中寻找余数等于60-t的个数累加即可

import collections
class Solution:
    def numPairsDivisibleBy60(self, time):
        c=collections.Counter()
        res=0
        for t in time:
            t=t%60
            res+=c[(60-t)%60]
            c[t]+=1
        return res