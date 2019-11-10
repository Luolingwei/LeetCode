
# 2的时候各自加1,0的时候各自加0,1的时候先给upper加，如果upper加完，再给lower加

import collections
class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
        count=collections.Counter(colsum)
        if count[2]>min(upper,lower): return []
        if upper+lower-count[2]*2!=count[1]: return []
        u,o=[],[]
        upper,lower=upper-count[2],lower-count[2]
        for i,n in enumerate(colsum):
            if n==2:
                u.append(1)
                o.append(1)
            elif n==0:
                u.append(0)
                o.append(0)
            else:
                if upper:
                    u.append(1)
                    o.append(0)
                    upper-=1
                else:
                    o.append(1)
                    u.append(0)
                    lower-=1
        return [u,o]

a=Solution()
print(a.reconstructMatrix(2,1,[1,1,1]))
print(a.reconstructMatrix(2,3,[2,2,1,1]))
print(a.reconstructMatrix(5,5,[2,1,2,0,1,0,1,2,0,1]))