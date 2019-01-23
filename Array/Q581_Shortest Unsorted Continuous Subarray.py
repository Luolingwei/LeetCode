class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #solution1
        # i,j=0,len(nums)-1
        # while nums[i]<min(nums[i+1:]):
        #     i+=1
        # while nums[j]>max(nums[:j]):
        #     j-=1
        # return j-i+1

        #solution2
        # n=len(nums)
        # if n==1:
        #     return 0
        # max_list,min_list=[0]*n,[0]*n
        # max_list[0],min_list[n-1]=nums[0],nums[n-1]
        # for i in range(1,n):
        #     max_list[i]=max(nums[i],max_list[i-1])
        # for j in range(n-2,-1,-1):
        #     min_list[j]=min(nums[j],min_list[j+1])
        #
        # i,j=0,n-1
        # while i<n-1 and nums[i]<=min_list[i+1]:
        #     i+=1
        # while j>0 and nums[j]>=max_list[j-1]:
        #     j-=1
        # return max(0,j-i+1)

        #solution3
        sorted_nums=sorted(nums)
        i,j= 0,len(nums)-1
        while i<len(nums) and sorted_nums[i]==nums[i]:
            i+=1
        while j>-1 and sorted_nums[j]==nums[j]:
            j-=1
        return max(0,j-i+1)

a=Solution()
print(a.findUnsortedSubarray([2,6,4,8,10,9,15]))
print(a.findUnsortedSubarray([1,2,3,4]))
print(a.findUnsortedSubarray([1]))
print(a.findUnsortedSubarray([1,2]))
print(a.findUnsortedSubarray([2,1]))
print(a.findUnsortedSubarray([1,2,3,4,6,5,7,8]))
print(a.findUnsortedSubarray([1,2,3,3,3]))
