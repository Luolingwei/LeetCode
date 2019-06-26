class Solution:
    def permuteUnique(self, nums):
        def dfs(array,path):
            if not array:
                ans.append(path)
            for i in range(len(array)):
                if i>0 and array[i]==array[i-1]: continue
                dfs(array[:i]+array[i+1:],path+[array[i]])
        nums.sort()
        ans=[]
        dfs(nums,[])
        return ans

a=Solution()
print(a.permuteUnique([1,1,2]))
print(a.permuteUnique([1,1,2,2]))