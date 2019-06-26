class Solution:
    #solution 1
    # def permute(self, nums):
    #     ans=[[]]
    #     for _ in range(len(nums)):
    #         temp=[]
    #         for path in ans:
    #             for num in nums:
    #                 if num not in path: temp.append(path+[num])
    #         ans=temp[:]
    #     return ans

    #solution 2 iterative  52 ms
    # def permute(self, nums):
    #     ans=[[]]
    #     for _ in range(len(nums)):
    #         ans=[path+[i] for path in ans for i in nums if i not in path]
    #     return ans

    #solution 3 dfs 48 ms
    def permute(self, nums):
        ans,N=[],len(nums)
        def dfs(array,path):
            if not array:
                ans.append(path)
            for i in range(len(array)):
                dfs(array[:i]+array[i+1:],path+[array[i]])
        dfs(nums,[])
        return ans

a=Solution()
print(a.permute([1,2]))
print(a.permute([1,2,3]))
print(a.permute([1,2,3,4]))