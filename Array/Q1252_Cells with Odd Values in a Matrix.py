
# 思路: 记录奇数的行和列即可，总数先加，奇数行*m+和奇数列*n
# 奇数行列碰到奇数行列，变偶数，减去两倍
# 奇数行列碰到偶数行列，还是奇数，不减，只加过一次
# 偶数行列碰到偶数行列，偶数，没加，不管

import collections
class Solution:
    def oddCells(self, n,m,indices):
        oddr,oddc=0,0
        rows,cols=collections.Counter(),collections.Counter()
        for x,y in indices:
            rows[x]+=1
            cols[y]+=1
        for r in rows:
            if rows[r]%2:
                oddr+=1
        for c in cols:
            if cols[c]%2:
                oddc+=1
        return oddr*m+oddc*n-2*oddr*oddc

a=Solution()
print(a.oddCells(2,3,[[0,1],[1,1]]))
print(a.oddCells(2,2,[[1,1],[0,0]]))