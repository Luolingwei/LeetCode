# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].

# 思路1: 暴力解法，找出所有的i,j开头组合，往后延伸数列，更新最大长度.
# 思路2: dp, dp[i][j]表示以i和j结尾的最长数列长度，dp[i][j]=dp[idx[A[j]-A[i]]][i]+1
# 思路3: 改进dp: 因为是严格递增数组，所以可以直接用数字为index构建dp，dp的形式为collections.defaultdict(int), dp[(A[i],A[j])]=dp.get((A[j]-A[i],A[i]),2)+1

import collections
class Solution:
    # Solution 1 brute force 1200 ms
    # def lenLongestFibSubseq(self, A):
    #     s,N,ans=set(A),len(A),2
    #     for i in range(N):
    #         for j in range(i+1,N):
    #             a,b,l=A[i],A[j],2
    #             while a+b in s:
    #                 a,b,l=b,a+b,l+1
    #             ans=max(ans,l)
    #     return ans if ans>2 else 0

    # Solution 2 dp 964 ms
    # def lenLongestFibSubseq(self, A):
    #     idx={A[i]:i for i in range(len(A))}
    #     dp=[[2]*len(A) for _ in range(len(A))]
    #     for j in range(len(A)):
    #         for i in range(j):
    #             if A[j]-A[i] in idx and A[j]-A[i]<A[i]:
    #                 dp[i][j]=dp[idx[A[j]-A[i]]][i]+1
    #     ans=max(j for i in dp for j in i)
    #     return ans if ans>2 else 0

    # Solution 3 improved dp 480 ms
    def lenLongestFibSubseq(self, A):
        dp=collections.defaultdict(int)
        s=set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j]-A[i] in s and A[j]-A[i]<A[i]:
                    dp[(A[i],A[j])]=dp.get((A[j]-A[i],A[i]),2)+1
        return max(dp.values() or [0])

a=Solution()
print(a.lenLongestFibSubseq([1,3,5]))
print(a.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(a.lenLongestFibSubseq([1,3,7,11,12,14,18]))