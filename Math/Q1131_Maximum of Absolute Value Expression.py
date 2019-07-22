# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13

# 思路: 将绝对值符号展开，可以发现，一共有四种情况
# 1  (1[i]+2[i]+i)-(1[j]+2[j]+j)
# 2  (1[j]-2[j]-j)-(1[i]-2[i]-i)
# 3  (1[i]-2[i]+i)-(1[j]-2[j]+j)
# 4  (1[j]+2[j]-j)-(1[i]+2[i]-i)

# 因为括号内的公式一样，可以概括为(formula)最大值减最小值，此时式子取得最大值
# 最终取得最大值的地方一定是四种情况中的一种，所以取四个公式的最大值即可.

class Solution:
    def maxAbsValExpr(self, A, B):
        f1,f2,f3,f4=[],[],[],[]
        N=len(A)
        for i in range(N):
            f1+=[A[i]+B[i]+i]
            f2+=[A[i]+B[i]-i]
            f3+=[A[i]-B[i]+i]
            f4+=[A[i]-B[i]-i]
        return max(max(sub)-min(sub) for sub in [f1,f2,f3,f4])

a=Solution()
print(a.maxAbsValExpr([1,2,3,4],[-1,4,5,6]))
print(a.maxAbsValExpr([1,-2,-5,0,10],[0,-2,-1,-7,-4]))