# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return

# celebrity 不知道任何人，但所有人知道他
# 思路1: 用入度和出度进行判断, 相当于brute force
# O(n^2)

# 思路2: 事实上，每次比较两个人都可以排除1个
# 如果 i 知道 j, 那么i不可能成为名人,
# 如果 i 不知道 j, 那么j不可能成为名人,
# 所以只需要比较n-1次就可以剩下唯一的candidate
# 再次对candidate进行判断即可
# 对于candidate能确定的是他不知道他之后的所有人, 这里可以稍微简化一下

class Solution:
    # def findCelebrity(self, n):
    #     indegree,outdegree = [0]*n, [0]*n
    #     for i in range(n):
    #         for j in range(n):
    #             if i!=j and knows(i,j):
    #                 indegree[j]+=1
    #                 outdegree[i]+=1
    #     for i in range(n):
    #         if outdegree[i]==0 and indegree[i]==n-1:
    #             return i
    #     return -1

    def findCelebrity(self, n):
        res = 0
        for i in range(1,n):
            if knows(res,i):
                res = i
        for i in range(n):
            if i<res:
                if knows(res,i) or not knows(i,res):
                    return -1
            elif not knows(i,res):
                    return -1
        return res