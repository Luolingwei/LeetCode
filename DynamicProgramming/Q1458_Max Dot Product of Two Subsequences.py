
# 思路:
# 这里选取任意对即可(题目规定至少选1对)
# dp[i][j]表示nums1前i部分和nums2前j部分可以取得的最大值, 碰到负数可以不选, 所以初始化为0
# 如果最后一个都没选, 与题目不符, 说明没有同号的一对
# 都不选的情况是一个全正，一个全负。直接返回max(n1max*n2min,n2max*n1min)

class Solution:
    def maxDotProduct(self, nums1, nums2):
        n1max,n2max,n1min,n2min= max(nums1),max(nums2),min(nums1),min(nums2)
        if n1max*n2max<0 and n1min*n2min<0: return max(n1max*n2min,n2max*n1min)
        m,n = len(nums1),len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j-1]+nums1[i-1]*nums2[j-1],dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

a=Solution()
print(a.maxDotProduct([2,1,-2,5],[3,0,-6]))
print(a.maxDotProduct([3,-2],[2,-6,7]))
print(a.maxDotProduct([-1,-1],[1,1]))