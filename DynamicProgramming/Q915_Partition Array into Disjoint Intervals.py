# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]

# 思路: 判断条件为左边数组的最大值<=右边数组的最小值, dp建立右边的min数组，从左到右用curMax判断

class Solution:
    def partitionDisjoint(self, A):
        Amin,N=A[:],len(A)
        for i in range(N-1)[::-1]:
            Amin[i]=min(Amin[i+1],A[i+1])
        curMax=0
        for j in range(N):
            curMax=max(curMax,A[j])
            if curMax<=Amin[j]:
                return j+1

a=Solution()
print(a.partitionDisjoint([5,0,3,8,6]))
print(a.partitionDisjoint([1,1,1,0,6,12]))