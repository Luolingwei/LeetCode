class Solution:
    def canThreePartsEqualSum(self, A):
        total=sum(A)
        if total%3!=0: return False
        target,count,carry=total//3,0,0
        for num in A:
            carry+=num
            if carry==target:
                carry,count=0,count+1
        return carry==0 and count==3

a=Solution()
print(a.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(a.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(a.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
print(a.canThreePartsEqualSum([]))