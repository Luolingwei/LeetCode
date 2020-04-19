
# 思路: 分别收集字母和数字，比较个数，把个数多的先排即可

class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chars = []
        for c in s:
            if c.isalpha():
                chars.append(c)
            else:
                nums.append(c)
        if abs(len(chars)-len(nums))>1:
            return ""
        res = ""
        if len(nums)>=len(chars):
            while nums or chars:
                if nums: res += nums.pop()
                if chars: res += chars.pop()
        else:
            while nums or chars:
                if chars: res += chars.pop()
                if nums: res += nums.pop()
        return res

a=Solution()
print(a.reformat("a0b1c2"))
print(a.reformat("ab123"))