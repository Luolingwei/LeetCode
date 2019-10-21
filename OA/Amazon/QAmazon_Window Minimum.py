
# 注意存数组的index，window用单调栈存升序序列

class Solution:
    def min(self,nums,k):
        queue,ans=[],[]
        for i,n in enumerate(nums):
            while queue and n<nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i>=k-1:
                if queue[0]==i-k:
                    queue.pop(0)
                ans.append(nums[queue[0]])
        return ans

a=Solution()
print(a.min([1,2,3,4,5,6,7,8,9],3))
print(a.min([5,7,2,3,1,9,10,7],3))