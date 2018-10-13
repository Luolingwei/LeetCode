class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        i=0
        startpoint=None
        endpoint= None

        if nums==[]:
            return [-1,-1]
        if l==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]

        while i<l:
            if startpoint==None:
                if nums[i]==target:
                    startpoint=i
                else:
                    i=i+1
            else:
                if endpoint == None:
                    if nums[i]!=target:
                        endpoint=i-1
                    else:
                        i=i+1

            if startpoint!=None and endpoint!=None:
                break

        if startpoint == None and endpoint == None:
            return [-1,-1]
        elif startpoint!=None and endpoint== None:
            return [startpoint,l-1]
        else:
            return [startpoint,endpoint]

a=Solution()
print(a.searchRange([1,4,6],4))
print(a.searchRange([1,4,4,4,4,4,4],4))
print(a.searchRange([4,4,4,4,4,4,1,1],4))
print(a.searchRange([4,5,5,5,5,6,7],5))
print(a.searchRange([1,5,6,7,8,9,10],6))
