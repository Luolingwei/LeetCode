# Input: [1,17,8]
# Output: 2
# Explanation:
# [1,8,17] and [17,8,1] are the valid permutations.

# 思路: 先构造可以和每个数字形成完全平方数的dic(相当于graph)，然后通过dfs往后面累加数字，并改变Counter的记录数，True的条件是所有数字都被用到(dfs过程中left记录还剩余的数字个数)

import collections
class Solution:
    def numSquarefulPerms(self, A):
        self.ans=0
        c=collections.Counter(A)
        conn={i:{j for j in c if int(((i+j)**0.5))**2==(i+j)} for i in c}
        def dfs(x,left):
            if not left:self.ans+=1
            c[x]-=1
            for y in conn[x]:
                if c[y]: dfs(y,left-1)
            c[x]+=1
        for n in c:
            dfs(n,len(A)-1)
        return self.ans

a=Solution()
print(a.numSquarefulPerms([1,17,8]))