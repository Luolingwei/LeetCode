class Solution:
    # Solution 1
    # def encode(self, num):
    #     if num==0: return ""
    #     n,pos=1,1
    #     while num>n*2:
    #         num-=n*2
    #         pos+=1
    #         n=n*2
    #     code=str(bin(num-1))[2:]
    #     return '0'*(pos-len(code))+code

    # Solution 2
    def encode(self, num):
        return str(bin(num+1))[3:]

a=Solution()
print(a.encode(5))
print(a.encode(23))