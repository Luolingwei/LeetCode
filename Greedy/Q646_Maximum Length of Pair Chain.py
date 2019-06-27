# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]

# 思路: Greedy,因为end总是越小越好，最小的end一定是最长chain的起点，所以以end排序，然后开始往后累加.

class Solution:
    # Solution 1 dfs TLE
    # def findLongestChain(self, pairs):
    #     N=len(pairs)
    #     dp=[0]*N
    #     def dfs(i):
    #         if not dp[i]:
    #             dp[i]=1
    #             for j in range(N):
    #                 if pairs[j][0]>pairs[i][1]:
    #                     dp[i]=max(dp[i],dfs(j)+1)
    #         return dp[i]
    #     for i in range(N):
    #         dfs(i)
    #     return max(dp)

    # Solution 2 dp  2316 ms
    # def findLongestChain(self, pairs):
    #     pairs.sort(key=lambda x:x[1])
    #     dp=[1]*len(pairs)
    #     for i in range(len(pairs)):
    #         for j in range(i):
    #             if pairs[i][0]>pairs[j][1]:
    #                 dp[i]=max(dp[i],dp[j]+1)
    #     return max(dp)

    # Solution 3 Greedy 60 ms
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x:x[1])
        curEnd,ans=float('-inf'),0
        for pair in pairs:
            if pair[0]>curEnd:
                ans+=1
                curEnd=pair[1]
        return ans

a=Solution()
print(a.findLongestChain([[1,2], [2,3], [3,4]]))
print(a.findLongestChain([[3,4],[1,2], [2,3]]))