import heapq
#       2   4   6
#    +------------
#  1 |  3   5   7
#  7 |  9  11  13
# 11 | 13  15  17
# 思路:如果每个pop出的元素都加入右边和下面的元素，那么可以保证每次可以输出最邻近的最小值
# 但是会出现重复，所以为了避免重复，只在第一列pop的时候加入右边和下面元素，其他情况只加入右边元素
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        queue=[]
        def push(i,j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j],i,j])
        ans=[]
        push(0,0)
        while queue and len(ans)<k:
            _,i,j=heapq.heappop(queue)
            ans.append([nums1[i],nums2[j]])
            push(i,j+1)
            if j==0:
                push(i+1,0)
        return ans

a=Solution()
print(a.kSmallestPairs([2,4,6],[1,7,10],3))
print(a.kSmallestPairs([1,1,2],[1,2,3],2))
print(a.kSmallestPairs([1,2],[3],3))
print(a.kSmallestPairs([1],[],3))
print(a.kSmallestPairs([1,1,2],[1,2,3],10))