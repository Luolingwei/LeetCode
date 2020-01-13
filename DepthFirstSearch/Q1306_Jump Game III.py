
# 思路: 从start开始dfs寻找，用visited记录已经访问过的节点，直到找到0或遍历所有能遍历的节点

class Solution:
    def canReach(self, arr, start):
        visited=set()
        N=len(arr)
        def dfs(i):
            if 0<=i<N and i not in visited:
                if arr[i]==0: return True
                visited.add(i)
                return dfs(i+arr[i]) or dfs(i-arr[i])
            return False
        return dfs(start)

a=Solution()
print(a.canReach([4,2,3,0,3,1,2],5))