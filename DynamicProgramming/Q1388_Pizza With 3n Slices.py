import functools

# 问题转化为选择N//3个不相邻的数字, 和最大
# 类似House Robber 2, 两种情况, 没有头或者没有尾(头尾不可能同时被选)
# 不同的是, 这里限制了选N//3个, 将被选的数字从左到右考虑
# dp(i,j,k)表示从i到j选k个数能得到的最大和, 从左到右选可以固定右边j不变
# dp(i,j,k) = max(dp(i+2,j,k-1)+A[i],dp(i+1,j,k)), 选A[i]和不选A[i]
# bottom case是, k=1, 在剩下的数组中选最大的
# 提前终止条件: 数组长度<2*k-1时, 不可能在剩下的数组中选k个了, 返回负无穷
# 注意这里在i到j选k个时, 有1个朋友选的会落在范围之外, 所以最少2*k-1可以选k个, 比如3个数自己可以选2个

class Solution:
    def maxSizeSlices(self, A):
        N = len(A)
        n = N//3
        @functools.lru_cache(None)
        def dp(i,j,k):
            if k==1: return max(A[i:j+1])
            if j-i+1<2*k-1: return float('-inf')
            return max(dp(i+2,j,k-1)+A[i],dp(i+1,j,k))
        return max(dp(0,N-2,n),dp(1,N-1,n))

a=Solution()
print(a.maxSizeSlices([1,2,3,4,5,6]))
print(a.maxSizeSlices([8,9,8,6,1,1]))
print(a.maxSizeSlices([4,1,2,5,8,3,1,9,7]))
print(a.maxSizeSlices([3,1,2]))