# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# 思路: 和排序好的数字对比，从前到后搜索，找到第一个不相等的数字n，将数组A后面的最后一个n提到前面.

class Solution:
    def maximumSwap(self, num):
        A=list(str(num))
        B=sorted(A,reverse=True)
        for i in range(len(A)):
            if A[i]!=B[i]:
                j=len(A)-1-A[::-1].index(B[i])
                A[i],A[j]=A[j],A[i]
                return int(''.join(A))
        return num

a=Solution()
print(a.maximumSwap(2736))
print(a.maximumSwap(9973))
print(a.maximumSwap(2776))
print(a.maximumSwap(12))
print(a.maximumSwap(98368))
print(a.maximumSwap(10909091))