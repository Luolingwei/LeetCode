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

class Solution:
    # Solution 1 44 ms
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

    # Solution 2
    def mctFromLeafValues(self, arr):
        ans=0
        for n in sorted(arr)[:-1]:
            idx_min=arr.index(n)
            left=arr[idx_min-1] if idx_min>0 else float('inf')
            right=arr[idx_min+1] if idx_min<len(arr)-1 else float('inf')
            ans+=min(left,right)*n
            arr.pop(idx_min)
        return ans

a=Solution()
print(a.mctFromLeafValues([6,2,4]))