
# 思路: 递归提取因子, n%i==0时候对n//i提取因子
# 注意后面提取的因子要>=i, 否则会产生重复, 所以设置minx参数
# 另外最多提取到 math.sqrt(n), 因为后面后面会和前面重复
# Base case: 如果对某个数无法提取因子, 返回[[n]], 返回时排除自身即可

import math
class Solution:
    def getFactors(self, n):
        def dfs(minx,n):
            res = [[n]]
            for i in range(minx,int(math.sqrt(n))+1):
                if n%i==0:
                    res += [[i]+fs for fs in dfs(i,n//i)]
            return res
        return dfs(2,n)[1:]


a=Solution()
print(a.getFactors(12))
print(a.getFactors(32))