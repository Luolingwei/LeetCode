class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index=-1
        while digits[index]==9 and index>-len(digits):
            digits[index]=0
            index-=1
        if digits[index]!=9:
            digits[index]+=1
        else:
            digits[index]=0
            digits.insert(0,1)
        return digits

a=Solution()
print(a.plusOne([1,2,3]))
print(a.plusOne([4,3,2,1]))
print(a.plusOne([1,2,0,9]))
print(a.plusOne([7,9,9]))
print(a.plusOne([9,9,9]))
print(a.plusOne([9]))
