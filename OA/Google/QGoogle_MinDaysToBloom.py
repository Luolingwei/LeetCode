
# 思路: day作为binary search的目标, 找到最小的day满足>=n个花束即可

class Solution:
    def bloom(self, roses, n, k):
        def cal(day):
            x, res = 0, 0
            for r in roses:
                if r<=day:
                    x+=1
                else:
                    res += x//k
                    x = 0
            return res + x//k
        if len(roses)//k < n: return -1
        l, r = 0, max(roses)
        while l<r:
            mid = (l+r)//2
            if cal(mid)<n:
                l = mid + 1
            else:
                r = mid
        return l


a=Solution()
print(a.bloom([1,10,3,10,2],3,1))
print(a.bloom([1,10,3,10,2],3,2))
print(a.bloom([7,7,7,7,12,7,7],2,3))
print(a.bloom([1000000000,1000000000],1,1))
print(a.bloom([1,10,2,9,3,8,4,7,5,6],4,2))
