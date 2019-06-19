# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3

# 思路: 对于circular的，计算以当前idx结尾的最小数组，sum(A)-min即等于circular的最大值(sum是固定的). 对于非circular的，计算以当前idx结尾的最大数组
# 求两者的max即可.

class Solution:
    def maxSubarraySumCircular(self, A):
        if max(A)<0: return max(A)
        large,small=A[:],A[:]
        for i in range(1,len(A)):
            if large[i-1]>0: large[i]+=large[i-1]
            if small[i-1]<0: small[i]+=small[i-1]
        return max(max(large),sum(A)-min(small))

a=Solution()
print(a.maxSubarraySumCircular([1,-2,3,-2]))
print(a.maxSubarraySumCircular([5,-3,5]))
print(a.maxSubarraySumCircular([3,-1,2,-1]))
print(a.maxSubarraySumCircular([3,-2,2,-3]))
print(a.maxSubarraySumCircular([-2,-3,-1]))