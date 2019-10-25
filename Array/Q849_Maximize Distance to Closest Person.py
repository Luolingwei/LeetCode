
# 思路: 用last记录上一个访问到的Seat

class Solution:
    def maxDistToClosest(self, seats):
        ans,last,N=-1,-1,len(seats)
        for i,n in enumerate(seats):
            if n:
                ans=max(ans,(i-last)//2 if last>=0 else i-last-1)
                last=i
        return max(ans,N-last-1)