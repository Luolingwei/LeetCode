
# 思路: 排序之后Two Pointers，找小于K的最大Sum

class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        l,r=0,len(A)-1
        maxS=-1
        while l<r:
            curS=A[l]+A[r]
            if curS<K:
                if curS>maxS:
                    maxS=curS
                l+=1
            else:
                r-=1
        return maxS

a=Solution()
print(a.twoSumLessThanK([34,23,1,24,75,33,54,8],60))