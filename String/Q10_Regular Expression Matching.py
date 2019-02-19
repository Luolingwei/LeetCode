class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        table=[[False]*(len(s)+1) for _ in range(len(p)+1)]
        table[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                table[i][0]=table[i-2][0]
        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1]!='*':
                    table[i][j]=table[i-1][j-1] and (p[i-1]==s[j-1] or p[i-1]=='.')
                else:
                    table[i][j]=table[i-2][j] or (table[i][j-1] and (s[j-1]==p[i-2] or p[i-2]=='.'))
        return table[-1][-1]

a=Solution()
print(a.isMatch("aa",'a'))
print(a.isMatch("aa",'a*'))
print(a.isMatch("ab",'.*'))
print(a.isMatch("aab","c*a*b"))
print(a.isMatch("mississippi","mis*is*p*."))
