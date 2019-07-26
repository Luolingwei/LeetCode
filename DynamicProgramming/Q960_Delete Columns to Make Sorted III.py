# Input: ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
# Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.

# 思路: 删除最少的字母即寻找最长的递增序列
# 不同于寻找一个字符串的最长增序列，这里增的条件是all(dp[j]>dp[i] for word in A), dp[i]表示以i结尾的最长增序列

class Solution:
    def minDeletionSize(self, A):
        N=len(A[0])
        dp=[1]*N
        for j in range(1,N):
            for i in range(j):
                if all(word[j]>=word[i] for word in A):
                    dp[j]=max(dp[j],dp[i]+1)
        return N-max(dp)

a=Solution()
print(a.minDeletionSize(["babca","bbazb"]))
print(a.minDeletionSize(["edcba"]))
print(a.minDeletionSize(["ghi","def","abc"]))