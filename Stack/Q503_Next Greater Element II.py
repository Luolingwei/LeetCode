
# 思路1: 将A扩展为2倍原数组, 然后寻找Next Greater.
# 思路2: loop nums 两次，效果一样

class Solution:
    # def nextGreaterElements(self, nums):
    #     L=len(nums)
    #     A=nums+nums
    #     ans=[-1]*(2*L)
    #     stack=[]
    #     for i,n in enumerate(A):
    #         while stack and n>A[stack[-1]]:
    #             ans[stack.pop()]=n
    #         stack.append(i)
    #     return ans[:L]

    def nextGreaterElements(self, A):
        L=len(A)
        stack,res=[],[-1]*L
        for _ in range(2):
            for i,n in enumerate(A):
                while stack and A[stack[-1]]<n:
                    res[stack.pop()]=n
                stack.append(i)
        return res

a=Solution()
print(a.nextGreaterElements([1,2,1]))