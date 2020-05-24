
# 思路1: 用dfs搜索每一种可能的组合, 记录数字个数和总和, 看是否有符合条件的分割, TLE

# 思路2:
# 因为是分成两个平均值相等的数组, 所以两个数组的平均值一定等于整个平均值
# size较小的数组的长度范围是[1,N//2+1]
# 所以寻找target = avg*n(确保为整数) 的n个数字即可
# 用lru_cache进行缓存

import functools
class Solution:

    # def splitArraySameAverage(self, A):
    #     N = len(A)
    #     S = sum(A)
    #     def dfs(start,s,n):
    #         if 0<n<N and s*(N-n) == (S-s)*n:
    #             return True
    #         for i in range(start,N):
    #             if dfs(i+1,s+A[i],n+1):
    #                 return True
    #         return False
    #     return dfs(0,0,0)

    def splitArraySameAverage(self, A):
        N = len(A)
        S = sum(A)
        @functools.lru_cache(None)
        def dfs(target, count, i):
            if count == 0: return target == 0
            if target <= 0: return False
            if i + count > N: return False
            return dfs(target - A[i], count - 1, i + 1) or dfs(target, count, i + 1)

        return any(dfs((n * S) // N, n, 0) for n in range(1, N // 2 + 1) if (n * S) % N == 0)

a=Solution()
print(a.splitArraySameAverage([1,2,3,4,5,6,7,8]))
print(a.splitArraySameAverage([18,10,5,3]))
print(a.splitArraySameAverage([3863,703,1799,327,3682,4330,3388,6187,5330,6572,938,6842,678,9837,8256,6886,2204,5262,6643,829,745,8755,3549,6627,1633,4290,7]))