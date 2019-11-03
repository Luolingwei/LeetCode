
# 思路: 记录left括号个数和index，right不能匹配时加入drop，匹配时pop出left的index，最后剩下的left也加入drop

class Solution:
    # O(2n)
    def minRemoveToMakeValid(self, s):
        drop,leftidx=set(),[]
        for i,c in enumerate(s):
            if c=='(':
                leftidx.append(i)
            elif c==')':
                if not leftidx:
                    drop.add(i)
                else:
                    leftidx.pop()
        drop|=set(leftidx)
        return ''.join(c for i,c in enumerate(s) if i not in drop)

a=Solution()
print(a.minRemoveToMakeValid("lee(t(c)o)de)"))
print(a.minRemoveToMakeValid("a)b(c)d"))
print(a.minRemoveToMakeValid("))(("))
print(a.minRemoveToMakeValid("(a(b(c)d)"))