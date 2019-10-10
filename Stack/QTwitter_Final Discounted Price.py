
# 右边最近的小数，单调栈

class Solution:
    def discount(self,prices):
        stack=[]
        for i,p in enumerate(prices):
            while stack and p<=prices[stack[-1]]:
                prices[stack.pop()]-=p
            stack.append(i)
        return sum(prices),stack

a=Solution()
print(a.discount([2,3,1,2,4,2]))