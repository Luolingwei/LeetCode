from operator import *
class Solution:
    # Input: "2-1-1"
    # Output: [0, 2]
    # Explanation:
    # ((2 - 1) - 1) = 0
    # (2 - (1 - 1)) = 2
    # select the last operator
    def diffWaysToCompute(self, input):
        ops={'+':add,'-':sub,'*':mul,'/':truediv}
        ans=[]
        for i in range(len(input)):
            if input[i] in ops:
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])
                ans+=[ops[input[i]](l,r) for l in left for r in right]
        return ans or [int(input)]

a=Solution()
print(a.diffWaysToCompute("2-1-1"))
print(a.diffWaysToCompute("2*3-4*5"))