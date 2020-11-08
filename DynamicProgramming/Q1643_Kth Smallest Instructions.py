from math import comb

# 思路1: dfs, 从小到到 dfs 搜索string, 直到到达target的数量, TLE
# 思路2: math, 用组合数计算当前以H开头和以V开头的string个数
# 如果剩下的k大于H开头的数量, 直接跳过所有H, 加上"V", k-hstart
# 如果剩下的k小于等于H开头的数量, 说明一定是H开头, 加上"H", k不变


class Solution:
    def kthSmallestPath(self, destination, k):
        vn, hn = destination[0], destination[1]
        res = ""
        count = vn+hn
        for i in range(count):
            if not hn or not vn: break
            left_digit = count-i
            hstart = comb(left_digit-1,hn-1)
            if k>hstart:
                res += "V"
                k -= hstart
                vn -= 1
            else:
                res += "H"
                hn -= 1
        return res + "V"*vn + "H"*hn


a=Solution()
print(a.kthSmallestPath([2,3],1))
print(a.kthSmallestPath([2,3],2))
print(a.kthSmallestPath([2,3],3))
print(a.kthSmallestPath([10,13],970514))