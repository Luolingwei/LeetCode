
# 根据indegree和outdegree判断是否符合二叉树的规则
# indegree一定是1个0, n-1个1
# outdegree这里因为只有leftchild和rightchild所以不会超过2
# 排除孤立点, 即indegree+outdegree=0

class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        memo = [[0,0] for _ in range(n)]
        def assign(children):
            for parent,child in enumerate(children):
                if child!=-1:
                    memo[parent][1]+=1
                    memo[child][0]+=1
        assign(leftChild)
        assign(rightChild)
        indegree = [m[0] for m in memo]
        if max(indegree)>1 or sum(indegree)!=n-1:
            return False
        if min(map(sum,memo))==0 and n>1:
            return False
        return True


a=Solution()
print(a.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,-1,-1,-1]))
print(a.validateBinaryTreeNodes(4,[1,-1,3,-1],[2,3,-1,-1]))
print(a.validateBinaryTreeNodes(2,[1,0],[-1,-1]))
print(a.validateBinaryTreeNodes(6,[1,-1,-1,4,-1,-1],[2,-1,-1,5,-1,-1]))