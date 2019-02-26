import heapq
class Solution:
    # solution1 selection_sort
    # def findKthLargest(self, nums, k):
    #     for i in range(len(nums)):
    #         max=i
    #         for j in range(i+1,len(nums)):
    #             if nums[j]>nums[max]:
    #                 max=j
    #         nums[max],nums[i]=nums[i],nums[max]
    #         if i==k-1: return nums[i]

    # solution2 quick_sort
    # def findKthLargest(self, nums, k):
    #     return self.findKthSmallest(nums,len(nums)-k+1)
    #
    # def findKthSmallest(self, nums, k):
    #     if nums:
    #         index = self.partition(nums, 0, len(nums) - 1)
    #         if k > index + 1:
    #             return self.findKthSmallest(nums[index+1:], k-index-1)
    #         elif k < index + 1:
    #             return self.findKthSmallest(nums[:index], k)
    #         else:
    #             return nums[index]
    #
    # def partition(self, array, low, high):
    #     left = low
    #     key = array[low]
    #     while low < high:
    #         while array[high] >= key and low < high:
    #             high -= 1
    #         while array[low] <= key and low < high:
    #             low += 1
    #         array[low], array[high] = array[high], array[low]
    #     array[low], array[left] = array[left], array[low]
    #     return low

    #solution 3 heapq
    def findKthLargest(self, nums, k):
        heap=nums[:]
        heapq.heapify(heap)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

a=Solution()
print(a.findKthLargest([3,2,1,5,6,4],2))
print(a.findKthLargest([1],1))