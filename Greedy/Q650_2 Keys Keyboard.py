# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.

# 思路: Greedy, 当前的数量cur可以正好满足到达n的时候，copy下来，否则继续paste.

class Solution:
    def minSteps(self, n):
        cur,copy,step=1,0,0
        while cur<n:
            if not (n-cur)%cur: #当前的数量可以作为copy, copy下来
                copy=cur
                step+=1
            cur+=copy
            step+=1
        return step

a=Solution()
print(a.minSteps(3))
print(a.minSteps(10))