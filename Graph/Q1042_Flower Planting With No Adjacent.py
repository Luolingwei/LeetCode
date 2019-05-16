
# 思路: 因为每个像素最多有3个相邻像素，所以一定有可以涂的元素，用{1,2,3,4}减去其相邻元素涂的颜色，从中pop一个即可。

class Solution:
    def gardenNoAdj(self, N, paths):
        dic,res=[[] for _ in range(N)],[0]*N
        for x,y in paths:
            dic[x-1].append(y-1)
            dic[y-1].append(x-1)
        for i in range(N):
            res[i]=({1,2,3,4}-{res[j] for j in dic[i]}).pop()
        return res

a=Solution()
print(a.gardenNoAdj(3,[[1,2],[2,3],[3,1]]))
print(a.gardenNoAdj(4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
print(a.gardenNoAdj(1,[]))