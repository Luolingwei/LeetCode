
# 思路: 用一个flag标识是否位于{}内
# 如果在其中, 存储遇到的char,结束时进行expand, 否则直接expand

class Solution:
    def expand(self, S):
        res,stack,flag=[""],[],0
        for c in S:
            if c==',': continue
            if c=='{':
                flag=1
            elif c=='}':
                flag=0
                res=[s+c for s in res for c in stack]
                stack=[]
            elif flag==1:
                stack.append(c)
            elif flag==0:
                res=[s+c for s in res]
        return sorted(res)

a=Solution()
print(a.expand("{a,b}c{d,e}f"))
print(a.expand("abcd"))