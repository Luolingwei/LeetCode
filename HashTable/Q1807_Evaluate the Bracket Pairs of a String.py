
# 思路: 碰到'('和')'时更改flag, 根据flag把c加到res或者temp

class Solution:
    def evaluate(self, s: str, knowledge) -> str:
        memo = {k:v for k,v in knowledge}
        res, temp, flag = "", "", False
        for c in s:
            if c=='(':
                flag = True
            elif c==')':
                res += memo.get(temp,"?")
                temp = ""
                flag = False
            else:
                if flag: temp+=c
                else: res += c
        return res


a=Solution()
print(a.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))
print(a.evaluate("hi(name)", [["a","b"]]))
print(a.evaluate("(a)(a)(a)aaa", [["a","yes"]]))
print(a.evaluate("(a)(b)", [["a","b"],["b","a"]]))