class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length,count,dic=0,0,{0:-1}
        for i in range(len(nums)):
            count+=(1 if nums[i]==1 else -1)
            if count in dic:
                max_length=max(max_length,i-dic[count])
            else:
                dic[count]=i
        return max_length

a=Solution()
print(a.findMaxLength([1,0]))
print(a.findMaxLength([0,1,0,0,0,0,1,1]))

