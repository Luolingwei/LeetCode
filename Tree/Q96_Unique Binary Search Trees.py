# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 思路: dp[i]表示 1到i能构建的BST数量，在dp[i]中，root(j)可以选择1到i，dp[i] = dp[j-1](左子树) * j+1->i(右子树)(等价于dp[i-j])

class Solution:
    # Solution 1 iterative
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for root in range(1,i+1):
                dp[i]+=dp[root-1]*dp[i-root]
        return dp[n]

    # Solution 2 recursive
    # def numTrees(self, n):
    #     A=[float('-inf')]*(n+1)
    #     def dp(i):
    #         if A[i]==float('-inf'):
    #             if i==0: A[i]=1
    #             else:
    #                 A[i]=sum(dp(root-1)*dp(i-root) for root in range(1,i+1))
    #         return A[i]
    #     return dp(n)

a=Solution()
print(a.numTrees(3))
print(a.numTrees(4))
print(a.numTrees(5))