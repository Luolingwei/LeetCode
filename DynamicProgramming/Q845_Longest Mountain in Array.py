class Solution:
    def longestMountain(self, A):
        L=len(A)
        dp1,dp2=[1]*L,[1]*L
        for i in range(1,L):
            if A[i]>A[i-1]: dp1[i]=dp1[i-1]+1
        for j in range(L-2,-1,-1):
            if A[j]>A[j+1]: dp2[j]=dp2[j+1]+1
        return max([x+y for x,y in zip(dp1,dp2) if x>1 and y>1] or [1])-1

a=Solution()
print(a.longestMountain([2,1,4,7,3,2,5]))
print(a.longestMountain([2,2,2]))
print(a.longestMountain([]))