# Input: [1,2,2,3]
# Output: true
#
# Input: [6,5,4,4]
# Output: true

# 思路1: 初始化两个布尔值，分别代表递增和递减，然后更新
# 思路2: 用zip计算相邻数的gap，然后(i>j)-(i<j)判断是否有不同的状态(1和-1)

class Solution:
    # Solution 1
    # def isMonotonic(self, A):
    #     dec=inc=True
    #     for i in range(len(A)-1):
    #         if A[i]>A[i+1]: inc=False
    #         if A[i]<A[i+1]: dec=False
    #         if not any((dec,inc)): return False
    #     return dec or inc

    # Solution 2
    def isMonotonic(self, A):
        return not {(i>j)-(i<j) for i,j in zip(A,A[1:])}>={1,-1}

a=Solution()
print(a.isMonotonic([1,2,2,3]))