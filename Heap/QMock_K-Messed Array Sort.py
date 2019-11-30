
# 思路: 每个数字离正确位置最多为k，所以对每个数字搜索右边k的范围，找最小数放到当前位置即可，O(nk)
# 优化: 用heap存储每个k size的数字集合，到达k后pop出最小数放在最左边. O(nlogk)

import heapq
class Solution:
    # Solution 1 O(nk):
    # def sort_k_messed_array(self,arr, k):
    #     N=len(arr)
    #     for i in range(N):
    #         minidx,minN=i,arr[i]
    #         for j in range(i,min(N,i+k+1)):
    #             if arr[j]<minN:
    #                 minidx=j
    #                 minN=arr[j]
    #             arr[minidx],arr[i]=arr[i],arr[minidx]
    #     return arr

    # Solution 2 O(Nlogk)
    def sort_k_messed_array(self,arr, k):
        N=len(arr)
        curheap=[]
        for i in range(N):
            heapq.heappush(curheap,arr[i])
            if i>=k:
                arr[i-k]=heapq.heappop(curheap)
        j=i-k+1
        while curheap:
            arr[j]=heapq.heappop(curheap)
            j+=1
        return arr

a=Solution()
print(a.sort_k_messed_array([1,4,5,2,3,7,8,6,10,9],2))
print(a.sort_k_messed_array([1], 0))
print(a.sort_k_messed_array([1,0],1))
print(a.sort_k_messed_array([1,0,3,2], 1))