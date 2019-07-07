# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]

# 思路: 先找出整个字符串的最大深度，然后将大于一半深度的括号取出来即可.

class Solution:
    def maxDepthAfterSplit(self, seq):
        self.depth,ans=0,[0]*len(seq)
        def max_depth():
            d=0
            for char in seq:
                if char=='(':
                    d+=1
                    if d>self.depth:self.depth=d
                else:
                    d-=1
        max_depth()
        target_d,d2=self.depth//2,0
        for i,char in enumerate(seq):
            if char=='(':
                d2+=1
                if d2>target_d: ans[i]=1
            else:
                if d2>target_d: ans[i]=1
                d2-=1
        return ans

a=Solution()
print(a.maxDepthAfterSplit("()(())()"))
print(a.maxDepthAfterSplit("(((())))"))
print(a.maxDepthAfterSplit("(()())"))
print(a.maxDepthAfterSplit("(()(()))"))