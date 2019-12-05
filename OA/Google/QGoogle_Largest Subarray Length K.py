class Solution:
    # not unique
    # def find(self,array,k):
        # residx=0
        # curmax=window=''.join(map(str,array[:k]))
        # for i in range(1,len(array)-k+1):
        #     window=window[1:]
        #     window+=str(array[i+k-1])
        #     if window>curmax:
        #         residx=i
        #         curmax=window
        # return array[residx:residx+k]

    # unique
    def find(self,array,k):
        curmax,residx=float('-inf'),-1
        for i in range(len(array)-k+1):
            if array[i]>curmax:
                curmax=array[i]
                residx=i
        return array[residx:residx+k]

a=Solution()
print(a.find([1,4,3,2,5],4))
print(a.find([4,4,2,4,6],2))