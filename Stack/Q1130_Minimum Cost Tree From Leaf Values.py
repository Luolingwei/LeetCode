# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.
#
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4


# 思路1: 为了使大数被累成的次数尽量少，每次从最小数开始消，每次拿最小数和左右两边的小的那个一起消，小数pop，ans+=小数*min(left,right)，直到最后剩下一个数(最大数)
# 思路2: 为了消掉每个数，需要将这个数和比它大的数放一起，消掉的cost是n*min(l*r)，l>=a,r>=a. 问题变成寻找每个数左右最邻近的大数，用stack维护单调栈即可.

class Solution:
    # Solution 1 44 ms O(n^2)
    # def mctFromLeafValues(self, arr):
    #     self.ans=0
    #     def cal(arr):
    #         if len(arr)==1:
    #             return
    #         N=len(arr)
    #         idx=min([i for i in range(N-1)],key=lambda i:arr[i]*arr[i+1])
    #         self.ans+=arr[idx]*arr[idx+1]
    #         arr[idx]=max(arr[idx],arr[idx+1])
    #         arr.pop(idx+1)
    #         cal(arr)
    #     cal(arr)
    #     return self.ans

    # Solution 2 28 ms O(n^2)
    # def mctFromLeafValues(self, arr):
    #     ans=0
    #     for n in sorted(arr)[:-1]:
    #         idx_min=arr.index(n)
    #         left=arr[idx_min-1] if idx_min>0 else float('inf')
    #         right=arr[idx_min+1] if idx_min<len(arr)-1 else float('inf')
    #         ans+=min(left,right)*n
    #         arr.pop(idx_min)
    #     return ans

    # Solution 3 32ms O(n)
    def mctFromLeafValues(self, arr):
        stack,ans=[float('inf')],0
        for n in arr:
            while n>=stack[-1]:
                mid=stack.pop()
                ans+=mid*min(stack[-1],n)
            stack.append(n)
        while len(stack)>2:
            ans+=stack.pop()*stack[-1]
        return ans

a=Solution()
print(a.mctFromLeafValues([6,2,4]))
print(a.mctFromLeafValues([4,11]))