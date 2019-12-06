class Solution:
    def maxtime(self,s):
        strs=[c for c in s]
        for i,c in enumerate(strs):
            if c=='?':
                if i==0:
                    if strs[i+1]=='?' or strs[i+1]<='3':
                        strs[i]='2'
                    else:
                        strs[i]='1'
                elif i==1:
                    if strs[i-1]=='2':
                        strs[i]='3'
                    else:
                        strs[i]='9'
                elif i==3:
                    strs[i]='5'
                elif i==4:
                    strs[i]='9'
        return ''.join(strs)

a=Solution()
print(a.maxtime("?4:5?"))
print(a.maxtime("23:5?"))
print(a.maxtime("2?:22"))
print(a.maxtime("0?:??"))
print(a.maxtime("??:??"))
print(a.maxtime("0?:?8"))
print(a.maxtime("1?:4?"))
