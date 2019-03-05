class Solution:
    #solution1 one-line
    # def maxSlidingWindow(self, nums, k):
    #     return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

    #solution2 deque
    def maxSlidingWindow(self, nums, k):
        deque,ans=[],[]
        for i,num in enumerate(nums):
            while deque and nums[deque[-1]]<num:
                deque.pop()
            deque+=[i]
            if deque[0]==i-k:
                deque.pop(0)
            if i>=k-1:
                ans+=[nums[deque[0]]]
        return ans

a=Solution()
print(a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))