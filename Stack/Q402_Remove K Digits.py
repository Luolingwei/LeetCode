# Input: num = "1432219", k = 3
# Output: "1219"
#
# Input: num = "10200", k = 1
# Output: "200"
#
# Input: num = "10", k = 2
# Output: "0"

# 思路: 用stack存储每一个新来的数字，如果大于stack最后一个，则添加到stack中，如果小于stack最后一个，则向前pop stack中的比该元素大的元素。（靠前的位置要用更小的代替，以达到整体最小的效果）
# 如果循环出来k还没用完，说明原序列逆序的不够多，如'12345'，从后面删除k个元素即可。

class Solution:
    def removeKdigits(self, num, k):
        stack=[]
        for i in range(len(num)):
            while k and stack and num[i]<stack[-1]:
                stack.pop()
                k-=1
            stack.append(num[i])
        return ''.join(stack[:-k or None]).lstrip('0') or '0'


a=Solution()
print(a.removeKdigits('1432219',3))
print(a.removeKdigits('189100',2))
print(a.removeKdigits('10987100',2))
print(a.removeKdigits('10200',1))
print(a.removeKdigits('10',1))
print(a.removeKdigits('12345',2))
print(a.removeKdigits('10',2))