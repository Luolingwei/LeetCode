class Solution:
    def binary_search(self, list, target):
        if list==[]:
            return False
        mid=len(list)//2
        if list[mid]==target:
            return True
        elif list[mid]>target:
            return self.binary_search(list[:mid],target)
        else:
            return self.binary_search(list[mid+1:],target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums==[]:
            return False
        l=len(nums)
        startpoint=endpoint=None
        if nums[0]>target:
            startpoint=0
            while nums[startpoint]>target:
                startpoint+=1
                if startpoint==l:
                    break
        elif nums[0]==target:
            return True
        else:
            endpoint=l-1
            while nums[endpoint]<target:
                endpoint-=1
                if endpoint==-1:
                    break
        if endpoint==-1 or startpoint==0:
            return False
        elif startpoint==None and endpoint!=None:
            return self.binary_search(nums[:endpoint+1],target)
        elif endpoint==None and startpoint!=None:
            return self.binary_search(nums[startpoint:],target)

a=Solution()
print(a.search([2,5,6,0,0,1,2],0))
print(a.search([2,5,6,0,0,1,2],3))
print(a.search([1],3))
print(a.search([1,2],3))