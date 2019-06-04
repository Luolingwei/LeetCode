# Input: [2,1,2,6]
# Output: false

# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

# 思路: 用Count计数A中的数字，从最小的数开始，往前match，比如2往前match 4,4减去对应的个数

import collections

class Solution:
    def canReorderDoubled(self, A):
        A=collections.Counter(A)
        for n in sorted(A.keys(),key=abs):
            if A[n]>A[2*n]:
                return False
            A[2*n]-=A[n]
        return True

a=Solution()
print(a.canReorderDoubled([4,-2,2,-4]))
print(a.canReorderDoubled([2,1,2,6]))