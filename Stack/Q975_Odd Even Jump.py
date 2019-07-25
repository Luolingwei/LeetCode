# Input: [10,13,12,14,15]
# Output: 2
# Explanation:
# From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
# From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
# From starting index i = 3, we can jump to i = 4, so we've reached the end.
# From starting index i = 4, we've reached the end already.
# In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.

# 思路: 题目要求上下上下地交替跳
# 先找出每个index后面比它大的最小数或者比它小的最大数的index (以大小排序，用stack找)
# 然后用dp求各个位置是否可以作为向上或向下的起点，因为一开始odd要向上跳，所以sum(higher即可)

class Solution:
    def oddEvenJumps(self, A):
        N=len(A)
        next_h,next_l=[0]*N,[0]*N
        stack=[]
        for n,i in sorted((n,i) for i,n in enumerate(A)):
            while stack and i>stack[-1]:
                next_h[stack.pop()]=i
            stack.append(i)
        stack=[]
        for n,i in sorted((-n,i) for i,n in enumerate(A)):
            while stack and i>stack[-1]:
                next_l[stack.pop()]=i
            stack.append(i)
        higher,lower=[0]*N,[0]*N
        higher[-1],lower[-1]=1,1
        for j in range(N-1)[::-1]:
            higher[j]=lower[next_h[j]]
            lower[j]=higher[next_l[j]]
        return sum(higher)

a=Solution()
print(a.oddEvenJumps([10,13,12,14,15]))
print(a.oddEvenJumps([5,1,3,4,2]))
print(a.oddEvenJumps([50,28]))