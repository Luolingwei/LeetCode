# Input: "(*))"
# Output: True

# 思路: 用cmin,cmax表示所需要的最少')'和最多')'
# cmax<0表示遇到太多')', cmin最后大于0表示'('太多.
# 注意cmin要保持大于等于0, 因为cmin小于0的时候碰到了太多的')', 此时由cmax进行判断, cmin在后面重新从0开始统计

class Solution:
    def checkValidString(self, s):
        cmin,cmax=0,0
        for char in s:
            if char=='(':
                cmin+=1
                cmax+=1
            if char==')':
                cmin=max(cmin-1,0)
                cmax-=1
            if char=='*':
                cmin=max(cmin-1,0)
                cmax+=1
            if cmax<0: return False
        return cmin==0

a=Solution()
print(a.checkValidString("(((()**()((*)**("))
print(a.checkValidString("()"))
print(a.checkValidString("(*)"))
print(a.checkValidString("(*))"))
print(a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))