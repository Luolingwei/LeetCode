
# 由于grid面积无穷大，正常的dfs和bfs搜索会导致超时.
# 思路: 注意到block的最多像素为200，能围住的最大面积为0+1+2+....+199=19900<20000，所以分别判断起点和终点是否会被围住，如果都不会被围住，那么就能相连.

class Solution:
    # Solution 1 dfs
    # def isEscapePossible(self, blocked, source, target):
    #     blocked={tuple(i) for i in blocked}
    #     visited1,visited2=set(),set()
    #     def dfs(i,j,target,visited):
    #         if 0<=i<1000000 and 0<=j<1000000 and (i,j) not in visited and (i,j) not in blocked:
    #             if [i,j]==target or len(visited)>=20000: return True
    #             visited.add((i,j))
    #             return dfs(i+1,j,target,visited) or dfs(i-1,j,target,visited) or dfs(i,j+1,target,visited) or dfs(i,j-1,target,visited)
    #         return False
    #     return dfs(target[0],target[1],source,visited1) and dfs(source[0],source[1],target,visited2)

    # Solution 2 bfs
    def isEscapePossible(self, blocked, source, target):
        blocked={tuple(i) for i in blocked}
        visited1,visited2=set(),set()
        def bfs(source,target,visited):
            bfs=[tuple(source)]
            while bfs:
                x,y=bfs.pop(0)
                for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    new_x,new_y=x+dx,y+dy
                    if 0<=new_x<1000000 and 0<=new_y<1000000 and (new_x,new_y) not in visited and (new_x,new_y) not in blocked:
                        if [new_x,new_y]==target or len(visited)>=20000: return True
                        visited.add((new_x,new_y))
                        bfs.append((new_x,new_y))
            return False
        return bfs(source,target,visited1) and bfs(target,source,visited2)

a=Solution()
print(a.isEscapePossible([],[0,0],[999999,999999]))
print(a.isEscapePossible([[10,9],[9,10],[10,11],[11,10]],[0,0],[10,10]))