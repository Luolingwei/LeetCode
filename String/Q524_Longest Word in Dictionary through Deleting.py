
# 思路: 将d中的word以length和字母排序，然后依次check是否在s中即可，iter的使用非常精妙，顺序对比字符串.

class Solution:
    def findLongestWord(self, s, d):
        d.sort(key=lambda x: (-len(x),x))
        for word in d:
            it=iter(s)
            if all(char in it for char in word): return word
        return ''

a=Solution()
print(a.findLongestWord("abpcplea",["ale","apple","monkey","plea"]))
print(a.findLongestWord("abpcplea",["a","b","c"]))