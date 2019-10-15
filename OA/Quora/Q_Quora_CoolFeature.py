import collections
class Solution:
    def findtarget(self,a,b,query):
        countA,countB=collections.Counter(a),collections.Counter(b)
        ans=[]
        def helper(target):
            res=0
            for akey in countA:
                res+=countA[akey]*countB[target-akey]
            return res
        for q in query:
            if len(q)==2:
                ans.append(helper(q[1]))
            if len(q)==3:
                countB[b[q[1]]]-=1
                countB[q[2]]+=1
                b[q[1]]=q[2]
        return ans

a=Solution()
print(a.findtarget([1, 2, 3],[3,4],[[1, 5], [1, 1 , 1], [1, 5]]))