# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].

# 思路1: sliding window, eg: 匹配到长度为2的时候，window长度变为3，往后继续匹配(后面的2已经不需要check了，前面也不会有比2长的)
# 为了方便搜索，以及防止数字相连，如2,5变成25，将数字转成chr形式(0-255)

# 思路2: dp, dp[i][j]表示以A[i]和B[j]结尾的最长公共sub序列

class Solution:
    # Solution 1 sliding window
    def findLength(self, A, B):
        A,B=map(chr,A),''.join(map(chr,B))
        window=''
        for c in A:
            window+=c
            if window not in B:
                window=window[1:]
        return len(window)

    # Solution 2 dp
    # def findLength(self, A, B):
    #     m,n=len(A),len(B)
    #     dp=[[0]*(n+1) for _ in range(m+1)]
    #     for i in range(1,m+1):
    #         for j in range(1,n+1):
    #             if A[i-1]==B[j-1]:
    #                 dp[i][j]=dp[i-1][j-1]+1
    #     return max(j for sub in dp for j in sub)

a=Solution()
print(a.findLength([1,2,3,2,1,6],[3,2,1,4,7,8]))
print(a.findLength([1],[2]))
print(a.findLength([1],[1]))
print(a.findLength([0,1,1,1,1],[1,0,1,0,1]))