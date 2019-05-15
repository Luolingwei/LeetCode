# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# 思路: 将每一个字符串用二进制数表示，二进制数的每一位代表各个字母是否出现，用dic记录最大字符串长度，最后计算无相同字母（与操作为0）的最大字符串长度的乘积即可。
# 如 'abd'即表示为'1101'

class Solution:
    def maxProduct(self, words):
        dic={}
        for word in words:
            mask=0
            for char in set(word):
                mask|=(1<<ord(char)-ord('a')) # 'b'就是'10'
            dic[mask]=max(dic.get(mask,0),len(word))
        return max([dic[a]*dic[b] for a in dic for b in dic if not a&b] or [0])

a=Solution()
print(a.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))