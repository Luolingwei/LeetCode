# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

# 思路: dp(i,prev)表示完成i及其后面的排序需要的operation次数, 分为当前换和不换两种情况
# dp(i,prev)=min(dp(i+1,A[i]) if A[i]>prev, dp(i+1,B[j])+1), B[j]取B中比prev稍微大一点的

# T(n) = 2*T(n-1) + log(n)

import bisect
class Solution:
    def makeArrayIncreasing(self, A, B):
        B=sorted(set(B))
        m,n=len(A),len(B)
        memo={}
        def dp(i,prev):
            if (i,prev) not in memo:
                if i==m: return 0
                j=bisect.bisect_right(B,prev)
                memo[(i,prev)]=min(dp(i+1,A[i]) if A[i]>prev else float('inf'),dp(i+1,B[j])+1 if j<n else float('inf'))
            return memo[(i,prev)]
        ans=dp(0,float('-inf'))
        return ans if ans!=float('inf') else -1

a=Solution()
print(a.makeArrayIncreasing([1,5,3,6,7],[1,3,2,4]))
print(a.makeArrayIncreasing([1,5,3,6,7],[4,3,1]))
print(a.makeArrayIncreasing([1,5,3,6,7],[1,6,3,3]))