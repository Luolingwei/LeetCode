
# 每一轮根据规则更新以每个字母结尾的字符串个数即可

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u=1,1,1,1,1
        for _ in range(n-1):
            a,e,i,o,u=i+e+u,i+a,e+o,i,i+o
        return (a+e+i+o+u)%(10**9+7)

a=Solution()
print(a.countVowelPermutation(5))