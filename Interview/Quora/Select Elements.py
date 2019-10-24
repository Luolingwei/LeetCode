import collections
class Solution:
    # Solution 1 输入元素为1到N
    # def select(self,nums,N):
    #     c=collections.Counter(nums)
    #     sel=[0]*(N+1)
    #     nosel=[0]*(N+1)
    #     for i in range(1,N+1):
    #         carry=i*c[i]
    #         sel[i],nosel[i]=nosel[i-1]+carry,max(nosel[i-1],sel[i-1])
    #     return max(sel[N],nosel[N])

    # Solution 2 输入元素为任意值
    def select(self,nums):
        c=collections.Counter(nums)
        array,N=sorted(list(c.keys())),len(c)
        sel,nosel=[0]*N,[0]*N
        sel[0],nosel[0]=array[0]*c[array[0]],0
        for i in range(1,N):
            carry=array[i]*c[array[i]]
            if array[i]-array[i-1]>1:
                prev=max(nosel[i-1],sel[i-1])
                sel[i],nosel[i]=prev+carry,prev
            else:
                sel[i],nosel[i]=nosel[i-1]+carry,max(nosel[i-1],sel[i-1])
        return max(sel[-1],nosel[-1])


a=Solution()
print(a.select([1,1,2,3,4,4,5,5,6]))
print(a.select([1,1,1,1,1,1,1,1,1,1,2,3,4,4,4,4,4,4]))
print(a.select([6,5,5,5,3,5,4,4,4,3,6,5,3,1,1,6,8]))