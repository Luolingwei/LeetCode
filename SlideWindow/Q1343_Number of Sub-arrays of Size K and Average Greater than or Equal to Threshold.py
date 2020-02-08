
# 思路: sliding window 或者 presum，找size为k的subarray之和即可

class Solution:
    # solution 1 sliding window
    def numOfSubarrays(self, arr, k: int, threshold: int):
        limit=threshold*k
        curs=sum(arr[:k])
        res=int(curs>=limit)
        for i in range(k,len(arr)):
            curs=curs+arr[i]-arr[i-k]
            res+=(curs>=limit)
        return res

    # solution 2 presum
    # def numOfSubarrays(self, arr, k: int, threshold: int):
    #     N,res,limit=len(arr),0,threshold*k
    #     pres=[0]*(N+1)
    #     for i in range(1,N+1):
    #         pres[i]=pres[i-1]+arr[i-1]
    #     for j in range(k,N+1):
    #         res+=pres[j]-pres[j-k]>=limit
    #     return res

a=Solution()
print(a.numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
print(a.numOfSubarrays([1,1,1,1,1],1,0))
print(a.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5))
print(a.numOfSubarrays([7,7,7,7,7,7,7],7,7))
print(a.numOfSubarrays([4,4,4,4],4,1))