class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        S=list()
        a=0
        b=1
        c=2
        l=len(nums)
        while a<l:
            while b<l:
                while c<l:
                    if nums[a]+nums[b]+nums[c]==0:
                        answer_zero=[nums[a],nums[b],nums[c]]
                        S.append(answer_zero)
                    c=c+1
                b=b+1
                c=b+1
            a=a+1
            b=a+1
        return S

a=Solution()
print(a.threeSum([-1,0,1,2,-1,-4,8,-3,5,7]))