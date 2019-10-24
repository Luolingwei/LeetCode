class Solution:
    def modify(self,arrays):
        ans=float('inf')
        def helper(array):
            if array==[1,1,1]: return 0
            else:
                idx=array.index(max(array))
                array[idx]-=(sum(array)-array[idx])
                return helper(array)+1
        for array in arrays:
            ans=min(ans,helper(array))
        return ans


a=Solution()
print(a.modify([[1,3,5],[1,5,7],[3,9,13]]))

