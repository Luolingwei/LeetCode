class Solution:
    def addStrings(self, num1, num2):
        length1,length2=len(num1),len(num2)
        index1,index2,carry,ans=-1,-1,0,[]
        while index1>=-length1 or index2>=-length2 or carry>0:
            if index1>=-length1 and index2>=-length2:
                carry,reminder=divmod(int(num1[index1])+int(num2[index2])+carry,10)
            elif index1>=-length1 and index2<-length2:
                carry,reminder=divmod(int(num1[index1])+carry,10)
            elif index2>=-length2 and index1<-length1:
                carry,reminder=divmod(int(num2[index2])+carry,10)
            elif index1<-length1 and index2<-length2 and carry>0:
                carry,reminder=divmod(carry,10)
            ans.insert(0,str(reminder))
            index1-=1
            index2-=1
        return ''.join(ans)

a=Solution()
print(a.addStrings('123','678'))
print(a.addStrings('123','978'))
print(a.addStrings('9','99'))