
# 思路: 逐位进行比较，用1进行掩膜取到各个位的数字
# 如果ci=1,ai和bi有一个1即可
# 如果ci=0,ai和bi必须都为0

class Solution:
    def minFlips(self, a, b, c):
        res=0
        for i in range(32):
            ai,bi,ci=a&1,b&1,c&1
            if ci==1:
                res+=(ai+bi==0)
            else:
                res+=(ai+bi)
            a,b,c=a>>1,b>>1,c>>1
        return res

a=Solution()
print(a.minFlips(2,6,5))
print(a.minFlips(4,2,7))
print(a.minFlips(1,2,3))
print(a.minFlips(8,3,5))
