class Solution:
    def find(self,A,B):
        gaps=[A[i]-A[i-1] for i in range(1,len(A))]
        def helper(nums):
            small=min(nums)
            for i in range(1,small+1)[::-1]:
                if list(filter(lambda j:j%i!=0,nums))==[]:
                    return i
        g,add,setA,setB=helper(gaps),0,set(A),set(B)
        setAB=setA|setB
        curN,i=A[0],0
        while curN in setAB:
            if curN not in setA:
                add+=1
            curN+=g
        if curN-g <A[-1]: return -1
        curM=A[0]-g
        while curM in setB:
            add+=1
            curM-=g
        return len(A)+add

a=Solution()
print(a.find([0,4,8,20],[-4,5,7,12,16,22]))
print(a.find([0,4,8,12],[-4,5,7,12,16,22]))
print(a.find([0,4,8,9,12],[1,2,3,5,6,7,10,11,13]))
print(a.find([0,8,12],[2,4,5,6,10,11,13]))

