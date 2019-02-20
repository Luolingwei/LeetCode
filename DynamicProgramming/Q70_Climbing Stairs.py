class Solution:
    def climbStairs(self, n):
        table=[0]*(n+1)
        table[0],table[1]=1,1
        for i in range(2,n+1):
            table[i]=table[i-1]+table[i-2]
        return table[n]

a=Solution()
print(a.climbStairs(2))
print(a.climbStairs(3))
print(a.climbStairs(4))