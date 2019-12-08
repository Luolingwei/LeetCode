import collections
class Solution:
    def groupThePeople(self, groupSizes):
        memo=collections.defaultdict(list)
        res=[]
        for i,n in enumerate(groupSizes):
            memo[n].append(i)
            if len(memo[n])==n:
                res.append(memo[n])
                memo[n]=[]
        return res

a=Solution()
print(a.groupThePeople([3,3,3,3,3,1,3]))