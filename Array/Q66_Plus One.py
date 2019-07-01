class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry,new=1,[]
        while carry:
            carry,reminder=divmod(((digits or [0]).pop()+carry),10)
            new+=[reminder]
        return digits+new[::-1]

a=Solution()
print(a.plusOne([1,2,3]))
print(a.plusOne([4,3,2,1]))
print(a.plusOne([1,2,0,9]))
print(a.plusOne([7,9,9]))
print(a.plusOne([9,9,9]))
print(a.plusOne([9]))