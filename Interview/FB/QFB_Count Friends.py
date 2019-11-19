import collections
class Solution:
    def count(self,connect):
        graph=collections.defaultdict(int)
        for c in connect:
            if len(c)==2:
                graph[c[0]]+=1
                graph[c[1]]+=1
        return graph

a=Solution()
print(a.count([['A','B'],['A','C'],['C','B'],['B','D'],['E']]))