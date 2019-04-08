class Solution:
    # binary searcch
    def isPerfectSquare(self, num):
        left,right=1,num/2
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                left=mid+1
            else:
                right=mid-1
        return left*left==num

a=Solution()
print(a.isPerfectSquare(1))
print(a.isPerfectSquare(14))
print(a.isPerfectSquare(10564156384))