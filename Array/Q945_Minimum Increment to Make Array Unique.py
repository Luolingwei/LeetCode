# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].

# 思路: 将数组排序，如果A[i]小于等于A[i-1]，将A[i]置为A[i-1]+1，并累加ans

class Solution:
    # Solution 1 Greedy O(nlogn)
    def minIncrementForUnique(self, A):
        A.sort()
        ans=0
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                ans+=A[i-1]+1-A[i]
                A[i]=A[i-1]+1
        return ans


a=Solution()
print(a.minIncrementForUnique([3,2,1,2,1,7]))
print(a.minIncrementForUnique([1,2,2]))