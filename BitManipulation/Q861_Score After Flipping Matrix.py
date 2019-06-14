# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# 思路: 转换成二进制数进行考虑，每一列j位置的point是(1<<n-j-1)*A[i][j]，由于第一位A[i][0]的point大于后面的总和，所以把所有首位都变为1,这样改变之后，原来和首位相等的后面的数字变为1
# 为了使每一列1足够多，统计每个column和首列相同的个数，取相同(1)和不相同(0)的最大值(对列进行翻转)，乘以对应列的point.

class Solution:
    def matrixScore(self, A):
        m,n=len(A),len(A[0])
        ans=(1<<n-1)*m
        for j in range(1,n):
            ones=sum(A[i][j]==A[i][0] for i in range(m))
            ans+=max(ones,m-ones)*(1<<n-j-1)
        return ans

a=Solution()
print(a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))