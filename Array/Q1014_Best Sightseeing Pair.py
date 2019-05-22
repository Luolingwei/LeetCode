# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

# 思路: 每加入一个新的元素，计算它和前面“最佳元素”（A[i]+i）的总得分，更新ans和“最佳元素”

class Solution:
    def maxScoreSightseeingPair(self, A):
        pre=ans=float('-inf')
        for i in range(len(A)):
            ans=max(ans,A[i]-i+pre)
            pre=max(pre,A[i]+i)
        return ans

a=Solution()
print(a.maxScoreSightseeingPair([8,1,5,2,60]))
print(a.maxScoreSightseeingPair([2,1000]))