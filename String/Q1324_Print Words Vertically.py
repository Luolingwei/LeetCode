
# 思路: 先将所有word处理成同一长度，用zip函数对words进行横向提取，返回join和rstrip后的结果

class Solution:
    def printVertically(self, s):
        strs = s.split()
        maxL = max(map(len, strs))
        strs = [word + (maxL - len(word)) * ' ' for word in strs]
        return [''.join(t).rstrip() for t in zip(*strs)]

a=Solution()
print(a.printVertically("HOW ARE YOU"))
print(a.printVertically("TO BE OR NOT TO BE"))
print(a.printVertically("CONTEST IS COMING"))