
# 思路: 对状态进行分类
# 包含A: A(有一个A，结尾不是L)，AL(有一个A，结尾有一个L)，ALL(有一个A，结尾有两个L)
# 不包含A: P(没有A结尾也没有L)，PL(没有A，结尾有一个L)，PLL(没有A结尾有两个L)
# ans=sum(all)

class Solution:
    def checkRecord(self, n):
        mod=10**9+7
        A,AL,ALL,P,PL,PLL=0,0,0,0,0,0
        P=1
        for _ in range(n):
            A,AL,ALL,P,PL,PLL=sum([A,AL,ALL,P,PL,PLL])%mod,A,AL,sum([P,PL,PLL])%mod,P,PL
        return sum([A,AL,ALL,P,PL,PLL])%mod

a=Solution()
print(a.checkRecord(2))
print(a.checkRecord(1500))