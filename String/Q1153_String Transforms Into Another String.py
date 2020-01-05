
# 思路: 记录每个映射，出现之前有的不相符的映射返回False
# 至少要留一个临时temp作为中间转换字符，所以不能为26个字母

class Solution:
    def canConvert(self, str1, str2):
        if str1==str2: return True
        memo={}
        for i,j in zip(str1,str2):
            if memo.get(i,j)!=j:
                return False
            memo[i]=j
        return len(set(str2))<26