
# 思路: 从前往后扫描target，在target中进行匹配，source被扫描的次数(i被置为0的次数)为用source的个数

class Solution:
    def shortestWay(self, source, target):
        m,n=len(source),len(target)
        dic_s=set(source)
        i,j=0,0
        ans=0
        while j<n:
            if target[j] not in dic_s: return -1
            while i<m and target[j]!=source[i]:
                i+=1
            if i>=m:
                ans+=1
                i=0
            else:
                i,j=i+1,j+1
        return ans+(i!=0)

a=Solution()
print(a.shortestWay("abc","aaaaa"))
print(a.shortestWay("abc","abcbc"))
print(a.shortestWay("abc","acdbc"))
print(a.shortestWay("xyz","xzyxz"))
print(a.shortestWay("aaaaa","aaaaaaaaaaaaa"))
print(a.shortestWay("adbsc","addddddddddddsbc"))