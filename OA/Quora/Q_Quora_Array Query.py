import collections
from collections import Counter
from copy import deepcopy
class Solution:
    def Query(self,array,matrix):
        memo=collections.defaultdict(Counter)
        ans=0
        for i,n in enumerate(array):
            cur=deepcopy(memo[i-1])
            cur[n]+=1
            memo[i]=cur
        for l,r,target in matrix:
            ans+=memo[r][target]-memo[l-1][target]
        return ans

a=Solution()
print(a.Query([1,1,2,3,2],[[1,2,1],[2,4,2],[0,3,1]]))