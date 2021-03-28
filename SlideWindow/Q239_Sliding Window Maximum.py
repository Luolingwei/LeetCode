
# 思路: if deque[0]==i-k: deque.pop(0) 保证整个window在k的范围内.
# 每次进来一个新的元素，window中比它小的元素都可以pop，因为它们不可能成为max了,所以window中一直保持的是有用candidates的降序序列，ans每次加入window中的头部最大元素为作为max的值.

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