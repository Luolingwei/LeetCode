class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsize=0
        for i in range(len(nums)):
            size,k=0,i
            while nums[k]!=-1:
                index=nums[k]
                nums[k]=-1
                k=index
                size+=1
            maxsize=max(maxsize,size)
        return maxsize


a=Solution()
print(a.arrayNesting([5,4,0,3,1,6,2]))
