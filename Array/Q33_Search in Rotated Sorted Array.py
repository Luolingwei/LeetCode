class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return -1

        l=len(nums)

        if l==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        if target>= nums[0]:
            startpoint=0
            index=startpoint
            while index<l:
                if nums[index]==target:
                    return index
                elif index==l-1:
                    return -1
                elif nums[index]>nums[index+1]:
                    return -1
                else:
                    index=index+1

        else:
            startpoint=l-1
            index = startpoint
            while index>=0:
                if nums[index]==target:
                    return index
                elif index==0:
                    return -1
                elif nums[index]<nums[index-1]:
                    return -1
                else:
                    index=index-1

a=Solution()
print(a.search([4,5,6,7,0,1,2],1))
print(a.search([4,5,6,7,0,1,2],6))
print(a.search([4,5,6,7,0,1,2],9))
print(a.search([1,3],2))
print(a.search([3,2,1],3))





