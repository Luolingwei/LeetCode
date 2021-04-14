
# 思路: 每个str1中相同的c要对应str2中相同的c, 可以多对1: (a,b) -> (c,c)
# 如果映射出现了LinkedList: a->b->c->d, 可以倒着替换即可
# 如果映射出现了loop, a->b->c->a, 用一个temp替换掉loop中的1个字符即可, temp->b->c->a,
# 唯一映射相同的情况下 不能替换的case是: 没有unused temp字符, 即 a->b->c->...->a (26个字符均出现), 不管换成什么, 都会有loop
# 所以str2至少要保留1个temp字符, 否则一定会有26个字符的loop出现

class Solution:
    def canConvert(self, str1, str2):
        if str1==str2: return True
        memo={}
        for i,j in zip(str1,str2):
            if memo.get(i,j)!=j:
                return False
            memo[i]=j
        return len(set(str2))<26


a=Solution()
print(a.canConvert("aabcc", "ccdee"))
print(a.canConvert("leetcode", "codeleet"))
print(a.canConvert("abcdefghijklmnopqrstuvwxyz", "bcadefghijklmnopqrstuvwxzz"))