class Solution:
    '''
    say we have 1....n hats and 1....n people, the goal is that each person doesn't
    wear his own hat

    when there is n people,consider 1st person.

    he has n-1 choices, suppose he wears hat x

    if person x wears hat 1. Then remaining combinations are among n-2 people and n-2 hats. That should be dp[n-2]

    if person x doesn't wear hat 1. The remaining hats are 1...n except x. remaining people are 1...n except 1. We can imagine hat 1 as hat x, then 2 will choose hat other than 2, 3 other than 3, .... x other than x, ... n other than n. that should be dp[n-1]

    Total combinations: dp[n]=(n-1)*(dp[n-1]+dp[n-2])

    base case : dp[1],dp[2]=0,1

    '''
    def findDerangement(self, n: int) -> int:
        if n==1: return 0
        a,b,mod=0,1,10**9+7
        for i in range(3,n+1):
            a,b=b,((i-1)*(a+b))%mod
        return b%mod

a=Solution()
print(a.findDerangement(3))