import heapq
class Solution:
    def find(self,words,k):
        memo={}
        for w in words:
            memo[w]=memo.get(w,0)+1
        freq=[(-f,w) for w,f in memo.items()]
        heapq.heapify(freq)
        count=0
        visited=set()
        ans=[]
        while freq:
            f,w=heapq.heappop(freq)
            f=-f
            if f not in visited:
                count+=1
                visited.add(f)
                if count>k: break
            ans.append(w)
        return ans

a=Solution()
print(a.find(['a','a','b','b','c','d'],1))