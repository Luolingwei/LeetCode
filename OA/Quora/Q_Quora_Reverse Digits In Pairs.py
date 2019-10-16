class Solution:
    def reverse(self,s):
        signal=1
        if s<0: signal=-1
        s=abs(s)
        strs=[i for i in str(s)]
        for i in range(0,len(strs)-1,2):
            strs[i],strs[i+1]=strs[i+1],strs[i]
        return int(''.join(strs))*signal

a=Solution()
print(a.reverse(123456))
print(a.reverse(12345))
print(a.reverse(103458))
print(a.reverse(103458))
print(a.reverse(-103))