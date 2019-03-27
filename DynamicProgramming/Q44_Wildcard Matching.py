class Solution:
    def isMatch(self, s, p):
        table=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        table[0][0]=True
        for i in range(1,len(p)+1):
            table[0][i]=table[0][i-1] and p[i-1]=='*'
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]!='*':
                    table[i][j]=table[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='?')
                else:
                    table[i][j]=table[i-1][j] or table[i][j-1]
        return table[-1][-1]

a=Solution()
print(a.isMatch("adceb","*a*b"))
print(a.isMatch("aa","*"))