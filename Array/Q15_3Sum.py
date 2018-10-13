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
        nums.sort()
        l=len(nums)
        while a<l:
            if nums[a]>0:
                break;
            while b<l:
                while c<l:
                    if nums[a]+nums[b]+nums[c]==0:
                        answer_zero=[nums[a],nums[b],nums[c]]
                        if answer_zero not in S:
                            S.append(answer_zero)
                    c=c+1
                b=b+1
                c=b+1
            a=a+1
            b=a+1
            c=b+1
        return S

a=Solution()
print(a.threeSum([4,7,3,2,-4]))
print(a.threeSum([-1,-1,2,-1,-1,2,2,-4,1]))
print(a.threeSum([0,5,9,6,16,12,18,8,-5,-4,-2,-6]))