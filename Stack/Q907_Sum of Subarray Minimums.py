# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

# 思路: 用单调栈记录每个数字左边和右边比它大的连续数的边界，以该数字为最小值的子数组数量=(i-left)*(right-i)

class Solution:
    # solution 1 dp, TLE
    # def sumSubarrayMins(self, A):
    #     dp=[[i] for i in A]
    #     for i in range(1,len(A)):
    #         dp[i]+=[min(A[i],sub) for sub in dp[i-1]]
    #     return sum(i for sub in dp for i in sub)%(10**9+7)

    # solution 2 stack
    def sumSubarrayMins(self, A):
        s1,s2,N=[],[],len(A)
        left,right=[0]*N,[0]*N
        for i in range(N):
            while s1 and A[s1[-1]]>=A[i]:
                s1.pop()
            left[i]=s1[-1] if s1 else -1
            s1.append(i)
        for j in range(N)[::-1]:
            while s2 and A[s2[-1]]>A[j]: #防止出现重复数字
                s2.pop()
            right[j]=s2[-1] if s2 else N
            s2.append(j)
        return sum((i-left[i])*(right[i]-i)*A[i] for i in range(N))%(10**9+7)

a=Solution()
print(a.sumSubarrayMins([3,1,2,4]))
print(a.sumSubarrayMins([71,55,82,55]))