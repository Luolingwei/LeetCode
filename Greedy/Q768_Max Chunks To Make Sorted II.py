# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

# 思路1: 比较排序后的数组和原数组，两个数组元素完全一样的地方为可以作为分割的点
# 思路2: 直接比较排序后数组和原数组的sum值，如果两个sum一样，那么可以判断范围内的元素一样
# 思路3: 数组可以切割的条件可以是左边的最大值小于等于右边的最小值，所以先计算好min_l和max_r即可

import collections
class Solution:
    # # Solution 1 O(n*nlogn) 272 ms
    # def maxChunksToSorted(self, arr):
    #     A,B=collections.Counter(),collections.Counter()
    #     ans=0
    #     for a,b in zip(arr,sorted(arr)):
    #         A[a]+=1
    #         B[b]+=1
    #         ans+=A==B
    #     return ans
    #
    # # Solution 2 O(nlogn) 120 ms
    # def maxChunksToSorted(self, arr):
    #     sumA,sumB,ans=0,0,0
    #     for a,b in zip(arr,sorted(arr)):
    #         sumA+=a
    #         sumB+=b
    #         ans+=sumA==sumB
    #     return ans

    # Solution 3 O(n) 92 ms
    def maxChunksToSorted(self, arr):
        N,ans=len(arr),0
        max_l,min_r=[0]*N,[0]*(N-1)+[float('inf')]
        max_l[0]=arr[0]
        for i in range(1,N):
            max_l[i]=max(max_l[i-1],arr[i])
        for j in range(N-2,-1,-1):
            min_r[j]=min(min_r[j+1],arr[j+1])
        for k in range(N):
            if max_l[k]<=min_r[k]:
                ans+=1
        return ans


a=Solution()
print(a.maxChunksToSorted([5,4,3,2,1]))
print(a.maxChunksToSorted([2,1,3,4,4]))