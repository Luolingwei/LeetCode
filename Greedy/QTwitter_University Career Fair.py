import collections
class Solution:
    def findevents(self,arrs,durs):
        L=len(arrs)
        inters=collections.defaultdict(lambda : float('inf'))
        for i in range(L):
             inters[arrs[i]]=min(inters[arrs[i]],arrs[i]+durs[i])
        gaps=sorted(inters.items())
        ans,end=0,-1
        for curStart,curEnd in gaps:
            if curStart>=end:
                ans+=1
                end=max(end,curEnd)
        return ans

a=Solution()
print(a.findevents([1,3,3,5,7],[2,2,1,2,1]))