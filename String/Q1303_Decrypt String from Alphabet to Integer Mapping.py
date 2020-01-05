
# 思路: 从后往前扫描，碰到#就cut两个字符，否则cut一个字符

class Solution:
    def freqAlphabets(self, s):
        ans=''
        i=len(s)-1
        while i>=0:
            if s[i]=='#':
                ans=chr(int(s[i-2:i])+96)+ans
                i=i-3
            else:
                ans=chr(int(s[i])+96)+ans
                i=i-1
        return ans