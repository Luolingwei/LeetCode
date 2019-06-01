
# 思路: 进制转换就是不断取模，然后将余数作为当前位的数字。这里Base为-2
# 为了防止余数出现负数，每次reminder<0的时候，将reminder+2，N+1,相当于少除了一个-2. 3/-2=-1余1 而不是 -2余-1

class Solution:
    def baseNeg2(self, N):
        if not N: return '0'
        ans=''
        while N:
            N,reminder=divmod(N,-2)
            if reminder<0:
                N,reminder=N+1,reminder+2
            ans=str(reminder)+ans
        return ans

a=Solution()
print(a.baseNeg2(0))
print(a.baseNeg2(3))
print(a.baseNeg2(2))
print(a.baseNeg2(11))