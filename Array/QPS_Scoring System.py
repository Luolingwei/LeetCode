class Solution:
    def score(self,n):
        def r1(n):
            return str(n).count('7')*5
        def r2(n):
            count,ans=0,0
            for c in str(n):
                if count>0 and count%2==0:
                    ans+=count//2
                if c=='2':
                    count+=1
                else:
                    count=0
            return ans*6
        def r3(n):
            stack=[]
            for i in str(n):
                if stack and ord(i)-ord(stack[-1][-1])==-1:
                    stack[-1]+=i
                else:
                    stack.append(i)
            return sum(len(s)**2 for s in stack)
        def r4(n):
            return 4 if n%3==0 else 0
        def r5(n):
            return 3*len([c for c in str(n) if int(c)%2==0])
        return r1(n)+r2(n)+r3(n)+r4(n)+r5(n)


a=Solution()
print(a.score(765))