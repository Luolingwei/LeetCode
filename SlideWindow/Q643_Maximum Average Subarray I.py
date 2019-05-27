class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window=biggest=sum(nums[:k])
        for i in range(k,len(nums)):
            window+=nums[i]
            window-=nums[i-k]
            biggest=max(biggest,window)
        return biggest/k

a=Solution()
print(a.findMaxAverage([1,12,-5,-6,50,3],4))
print(a.findMaxAverage([-1],1))