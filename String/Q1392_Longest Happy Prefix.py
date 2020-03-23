
# 思路: 类似dp, 用lhp(longest happy prefix)存储截止当前index的最长lhp长度
# 初始i=0,j=1，i和j向右移动，如果s[i]==s[j]，那么当前lhp为长度i+1
# 如果match一段之后s[i]!=s[j]，不能将i置为0重新扫，因为此时可能还有一部分和尾部match
# 直接使用lhp[i-1]，表示仍然match的长度，(前面头部和尾部match长度为lhp[i-1]，因为前面s和后面s是一样的，所以和尾部j match的长度也是lhp[j-1])

class Solution:
    # O(n)
    def longestPrefix(self, s: str) -> str:
        lhp = [0]*len(s)
        i,j = 0,1
        while j<len(s):
            if s[i]==s[j]:
                lhp[j]=i+1
                i+=1
                j+=1
            else:
                if i>0:
                    i=lhp[i-1]
                else:
                    j+=1
        return s[:lhp[-1]]


a=Solution()
print(a.longestPrefix("acccbaaacccbaac"))
print(a.longestPrefix("level"))
print(a.longestPrefix("leetcodeleet"))