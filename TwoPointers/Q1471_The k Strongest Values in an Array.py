
# 思路: 离median越远的越strong, 先sort, 然后从两头2-pointers加入res
# median的正确定义: (A[n//2]+A[(n-1)//2])/2

class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        N = len(arr)
        median = arr[(N-1)//2]
        i,j = 0,N-1
        res = []
        while i<=j and len(res)<k:
            if abs(arr[i]-median)>abs(arr[j]-median):
                res.append(arr[i])
                i+=1
            else:
                res.append(arr[j])
                j-=1
        return res

a=Solution()
print(a.getStrongest([1,2,3,4,5],2))
print(a.getStrongest([-7,22,17,3],2))