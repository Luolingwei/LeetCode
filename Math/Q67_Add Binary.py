class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans=''
        carry=0
        a=a[::-1]
        b=b[::-1]
        for i in range(max(len(a),len(b))+1):
            if i>len(a)-1 and i<=len(b)-1:
                n=int(b[i])+carry
            elif i>len(b)-1 and i<=len(a)-1:
                n = int(a[i])+carry
            elif i>len(a)-1 and i>len(b)-1:
                if carry==1:
                    n=carry
                else:break
            else:
                n= int(a[i])+int(b[i])+carry

            carry=0
            if n<2:
                ans+=str(n)
            elif n==2:
                ans+=str(0)
                carry=1
            else:
                ans+=str(1)
                carry=1
        return ans[::-1]

a=Solution()
print(a.addBinary("11","1"))
print(a.addBinary("1010","1011"))
print(a.addBinary("0","0"))