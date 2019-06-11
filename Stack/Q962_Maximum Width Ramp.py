# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation:
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

# 思路: 用一个stack存储从左边开始的下降数组，因为右边的大一点的数不可能成为解的左值.
# 然后从右边遍历数组，check每个大于stack尾部的数，pop并更新ans，因为这些尾部的数此时距离右边的值是最大的，所以不需要继续check.

class Solution:
    # solution 1 brute force, TLE
    # def maxWidthRamp(self, A):
    #     return max([j-i for i in range(len(A)) for j in range(i+1,len(A)) if A[j]>=A[i]] or [0])

    # solution 2 stack
    def maxWidthRamp(self, A):
        stack,ans=[],float('-inf')
        for i,value in enumerate(A):
            if not stack or value<A[stack[-1]]:
                stack.append(i)
        for j in range(len(A)-1,-1,-1):
            while stack and A[j]>=A[stack[-1]]:
                ans=max(ans,j-stack.pop())
        return ans

a=Solution()
print(a.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
print(a.maxWidthRamp([1,9,10,2,1,5,6,7,8]))
print(a.maxWidthRamp([10,9,10,2,1,5,6,7,8]))
print(a.maxWidthRamp([10,9,10,2,1,1,1,0]))
print(a.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))