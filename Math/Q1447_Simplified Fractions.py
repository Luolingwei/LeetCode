
# 思路: 分母为2到n, 分子为1到分母-1
# 如果分子分母互质, 则符合条件加入
# 否则有公因子, 相除之后之前一定已经考虑过, 跳过

import math
class Solution:
    # or we can use math.gcd
    def simplifiedFractions(self, n):
        def gcd(x,y):
            while y:
                x,y = y,x%y
            return x

        res = []
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(i,j)==1:res.append(str(j)+'/'+str(i))
        return res

a=Solution()
print(a.simplifiedFractions(1))
print(a.simplifiedFractions(2))
print(a.simplifiedFractions(3))
print(a.simplifiedFractions(4))