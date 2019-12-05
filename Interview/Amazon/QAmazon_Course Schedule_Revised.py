# Input: {1:[2,3],2:[4,3],3:[5,6],4:[],5:[],6:[5]}
# Target: 1
# Output: [6,5,3,4,2,1]

# 拓扑排序dfs

class Solution:
    def search(self,dic,target):
        self.ans=[]
        visited=set()
        def dfs(node):
            for relied in dic[node]:
                if relied not in visited:
                    dfs(relied)
            self.ans+=[node]
            visited.add(node)
        dfs(target)
        return self.ans

a=Solution()
print(a.search({1:[2,3],2:[4,3],3:[5,6],4:[6],5:[],6:[5]},1))