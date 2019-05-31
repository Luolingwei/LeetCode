
# 思路: 从最低位数向前考虑，如果最小值不等于最大值，那么最后一位一定会存在不同（有0有1），也就是合成之后尾部会变为0.

class Solution:

    # Solution 1 revursive
    # def rangeBitwiseAnd(self, m, n):
    #     if m==n:
    #         return m
    #     return self.rangeBitwiseAnd(m>>1,n>>1)<<1

    # Solution 2 iterative
    def rangeBitwiseAnd(self, m, n):
        count=0
        while m!=n:
            m>>=1
            n>>=1
            count+=1
        return m<<count

a=Solution()
print(a.rangeBitwiseAnd(5,7))