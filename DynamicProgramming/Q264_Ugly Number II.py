class Solution:
    def nthUglyNumber(self, n):
        table=[1]*n
        i2=i3=i5=0
        for i in range(1,n):
            table[i]=min(table[i2]*2,table[i3]*3,table[i5]*5)
            if table[i]==table[i2]*2:
                i2+=1
            if table[i]==table[i3]*3:
                i3+=1
            if table[i]==table[i5]*5:
                i5+=1
        return table[-1]

a=Solution()
print(a.nthUglyNumber(10))