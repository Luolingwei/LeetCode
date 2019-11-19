
# 思路1: left,stars分别记录'('和'*'的位置，遇到')'时，优先pop'('，最后剩下的left和stars比较
# 如果left比stars或star在left左边出现，return False

class Solution:
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

a=Solution()
print(a.checkValidString("(((()**()((*)**("))
print(a.checkValidString("()"))
print(a.checkValidString("(*)"))
print(a.checkValidString("(*))"))
print(a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))