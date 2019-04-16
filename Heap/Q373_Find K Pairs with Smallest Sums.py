import heapq
#       2   4   6
#    +------------
#  1 |  3   5   7
#  7 |  9  11  13
# 11 | 13  15  17
# 思路:如果每个pop出的元素都加入右边和下面的元素，那么可以保证每次可以输出最邻近的最小值 Solution 1
# 但是会出现重复，所以为了避免重复，只在第一列pop的时候加入右边和下面元素，其他情况只加入右边元素 Solution 2
# 注: heapq.heappop会默认按照list的第一个元素大小进行pop

class Solution:
    # Solution 1 with memory
    # def kSmallestPairs(self, nums1, nums2, k):
    #     if len(nums1)*len(nums2)==0: return []
    #     ans,queue,memory=[],[[nums1[0]+nums2[0],(0,0)]],{}
    #     while queue and len(ans)<k:
    #         _,(i,j)=heapq.heappop(queue)
    #         ans.append([nums1[i],nums2[j]])
    #         if i+1<len(nums1) and (i+1,j) not in memory:
    #             heapq.heappush(queue,[nums1[i+1]+nums2[j],(i+1,j)])
    #             memory[(i+1,j)]=1
    #         if j+1<len(nums2) and (i,j+1) not in memory:
    #             heapq.heappush(queue,[nums1[i]+nums2[j+1],(i,j+1)])
    #             memory[(i,j+1)]=1
    #     return ans


    # Solution 2 without memory
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1)*len(nums2)==0: return []
        queue=[[nums1[0]+nums2[0],0,0]]
        ans=[]
        while queue and len(ans)<k:
            _,i,j=heapq.heappop(queue)
            ans.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j+1],i,j+1])
            if j==0 and i+1<len(nums1):
                heapq.heappush(queue,[nums1[i+1]+nums2[0],i+1,0])
        return ans


a=Solution()
print(a.kSmallestPairs([2,4,6],[1,7,10],3))
print(a.kSmallestPairs([1,1,2],[1,2,3],2))
print(a.kSmallestPairs([1,2],[3],3))
print(a.kSmallestPairs([1],[],3))
print(a.kSmallestPairs([1,1,2],[1,2,3],10))