class Solution:
    def play(self,n,k):
        queue=list(range(1,n+1))
        cur,length,ans=0,n,[]
        while len(queue)>1:
            cur=(cur+k-1)%length
            ans.append(queue.pop(cur))
            length-=1
        return ans

a=Solution()
print(a.play(6,3))

