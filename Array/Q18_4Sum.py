class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        S=list()
        a=0
        b=1
        c=2
        d=3
        nums.sort()
        l=len(nums)
        while a<l:
            while b<l:
                while c<l:
                    while d<l:
                        if nums[a]+nums[b]+nums[c]+nums[d]==target:
                            answer_zero=[nums[a],nums[b],nums[c],nums[d]]
                            if answer_zero not in S:
                                S.append(answer_zero)
                        d=d+1
                    c=c+1
                    d=c+1
                b=b+1
                c=b+1
                d=c+1
            a=a+1
            b=a+1
            c=b+1
            d=c+1
        return S

a=Solution()
print(a.fourSum([4,7,3,2,-4,2,7,-1],2))
print(a.fourSum([-1,-1,2,-1,-1,2,2,-4,1,-6,5],0))
print(a.fourSum([0,5,9,6,16,12,18,8,-5,-4,-2,-6],3))