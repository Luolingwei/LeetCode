# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

# 思路: 以最后一个group为dp的对象, dp[len(A)][K]=max(dp[i][K-1]+avg(A[i:len(A)])), i从k-1到len(A)-1(前k-1个group的长度).

class Solution:
    def largestSumOfAverages(self, A, K):
        dp,cur=[[0]*(len(A)+1) for _ in range(K+1)],0
        for j in range(1,len(A)+1):
            cur+=A[j-1]
            dp[1][j]=cur/float(j)
        for n_group in range(2,K+1):
            for length in range(len(A)+1):
                curS=0
                for i in range(length-1,n_group-2,-1):
                    curS+=A[i]
                    dp[n_group][length]=max(dp[n_group][length],dp[n_group-1][i]+curS/float(length-i))
        return dp[-1][-1]

a=Solution()
print(a.largestSumOfAverages([9,1,2,3,9],3))
print(a.largestSumOfAverages([1,2,3,4,5,6,7],4))