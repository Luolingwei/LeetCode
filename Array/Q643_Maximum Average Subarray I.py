class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        biggest=total=sum(nums[:k])
        start=0
        for i in range(k,len(nums)):
            total-=nums[start]
            total+=nums[i]
            biggest=max(biggest,total)
            start+=1
        return biggest/k

a=Solution()
print(a.findMaxAverage([1,12,-5,-6,50,3],4))
