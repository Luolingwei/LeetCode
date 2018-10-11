class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # close=abs(nums[0]+nums[1]+nums[2]-target)+1
        close=1000000
        answer=nums[0]+nums[1]+nums[2]
        a=0
        b=1
        c=2
        l=len(nums)
        while a<l:
            while b<l:
                while c<l:
                    if abs(nums[a]+nums[b]+nums[c]-target)<close:
                        close=abs(nums[a]+nums[b]+nums[c]-target)
                        answer=(nums[a]+nums[b]+nums[c])
                    c=c+1
                b=b+1
                c=b+1
            a=a+1
            b=a+1
            c=b+1
        return answer

a=Solution()
print(a.threeSumClosest([0,9,7,-3,-1,-5,5],10))
print(a.threeSumClosest([-3,-1,2,5],2))
print(a.threeSumClosest([-3,-1,7,5,-4],0))