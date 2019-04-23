# s = "abc", t = "ahbgdc"
# True
#
# s = "axc", t = "ahbgdc"
# False

# 思路1: 依次考虑s中的元素，与t中的进行匹配，如果从前到后匹配到，则进行下一个元素的匹配，如果全部匹配到则index=len(s)，返回True. 如果t遍历完还有未匹配的元素，则返回False.
# 思路2: 依次考虑s中的元素，与t中的进行匹配，用index函数每次找到下一个s元素所在最靠前位置index，并在t[index:]中向后寻找剩下的元素，如果出现后面没有s元素的情况，返回False. 全部匹配到则返回True.

class Solution:
    # Solution 1
    # def isSubsequence(self, s, t):
    #     if not s: return True
    #     index=0
    #     for char in t:
    #         if char==s[index]:
    #             index+=1
    #         if index==len(s):
    #             return True
    #     return False

    # Solution 2
    def isSubsequence(self, s, t):
        index=0
        for char in s:
            if char not in t[index:]:
                return False
            index+=t[index:].index(char)+1
        return True

a=Solution()
print(a.isSubsequence('abbbb','abcb'))
print(a.isSubsequence('axc','ahbgdc'))
print(a.isSubsequence('ahbgdc','ahbgdc'))