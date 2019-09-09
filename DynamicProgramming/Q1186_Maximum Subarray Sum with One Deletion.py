# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

# 思路: dp0,dp1分别表示没有delete和有delete的以当前结尾的最大subarray

class Solution:
    def maximumSum(self, A) -> int:
        N=len(A)
        dp0,dp1,res=A[0],0,A[0]
        for i in range(1,N):
            dp0,dp1=max(dp0+A[i],A[i]),max(dp0,dp1+A[i])
            res=max(res,dp0,dp1)
        return res

a=Solution()
print(a.maximumSum([-2,-3,-1,-4]))
print(a.maximumSum([-1,-1,-1,-1]))