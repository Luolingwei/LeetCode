class Solution:
    def trailingZeroes(self, n):
        zeros,temp=0,5
        while temp<=n:
            zeros+=n//temp
            temp*=5
        return zeros

a=Solution()
print(a.trailingZeroes(5))
print(a.trailingZeroes(3))
print(a.trailingZeroes(30))