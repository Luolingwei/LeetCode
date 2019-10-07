import heapq
from random import randint
class Solution:
    # solution1 selection_sort O(kn)
    # def findKthLargest(self, nums, k):
    #     for i in range(len(nums)):
    #         max=i
    #         for j in range(i+1,len(nums)):
    #             if nums[j]>nums[max]:
    #                 max=j
    #         nums[max],nums[i]=nums[i],nums[max]
    #         if i==k-1: return nums[i]

    # solution2 quick_sort Time: n+n/2+n/4+...+1=2n-1=O(n) Space: O(1)
    def findKthLargest(self, nums, k):
        index = self.partition(nums)
        if len(nums) - index > k:
            return self.findKthLargest(nums[index + 1:], k)
        elif len(nums) - index < k:
            return self.findKthLargest(nums[:index], k - len(nums) + index)
        else:
            return nums[index]

    def partition(self, nums):
        low, high = 0, len(nums) - 1
        rdx=randint(low,high) #随机选择key random QS
        key=nums[rdx]
        nums[high],nums[rdx]=nums[rdx],nums[high]
        i = -1
        for j in range(high):
            if nums[j] < key:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    #solution 3 heapq O(n+klogn)
    # def findKthLargest(self, nums, k):
    #     heap=nums[:]
    #     heapq.heapify(heap)
    #     for _ in range(len(nums)-k):
    #         heapq.heappop(heap)
    #     return heapq.heappop(heap)

a=Solution()
print(a.findKthLargest([3,2,1,5,6,4],2))
print(a.findKthLargest([1],1))
print(a.findKthLargest([3,2,3,1,2,4,5,5,6],4))