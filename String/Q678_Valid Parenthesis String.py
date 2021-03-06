# Input: "(*))"
# Output: True

# 思路1: left,stars分别记录'('和'*'的位置，遇到')'时，优先pop'('，最后剩下的left和stars比较
# 如果left比stars或star在left左边出现，return False

# 思路2: 用cmin,cmax表示所需要的最少')'和最多')'
# cmax<0表示遇到太多')', cmin最后大于0表示'('太多.
# 注意cmin要保持大于等于0, 因为cmin小于0的时候碰到了太多的')', 此时由cmax进行判断, cmin在后面重新从0开始统计

class Solution:
    # Solution 1
    def checkValidString(self, s: str) -> bool:
        left,stars=[],[]
        for i,c in enumerate(s):
            if c=='*':
                stars.append(i)
            if c=='(':
                left.append(i)
            if c==')':
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        if len(left)>len(stars):
            return False
        while left:
            if left.pop()>stars.pop():
                return False
        return True

    # Solution 2
    # def checkValidString(self, s):
    #     cmin,cmax=0,0
    #     for char in s:
    #         if char=='(':
    #             cmin+=1
    #             cmax+=1
    #         if char==')':
    #             cmin=max(cmin-1,0)
    #             cmax-=1
    #         if char=='*':
    #             cmin=max(cmin-1,0)
    #             cmax+=1
    #         if cmax<0: return False
    #     return cmin==0

a=Solution()
print(a.checkValidString("(((()**()((*)**("))
print(a.checkValidString("()"))
print(a.checkValidString("(*)"))
print(a.checkValidString("(*))"))
print(a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))