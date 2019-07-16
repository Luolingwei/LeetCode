# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.

# 思路: bfs, 记录每一次move之后可能的状态，直到状态等于target，用visited记录已经访问的状态
# 如果不能得到答案，会因为全部visited退出循环，返回-1

class Solution:
    def slidingPuzzle(self, board):
        moves=[(1,3),(0,2,4),(1,5),(0,4),(1,3,5),(2,4)]
        target,start=[1,2,3,4,5,0],board[0]+board[1]
        queue,dist,visited=[start],0,{tuple(start)}
        def swap(i,j,state):
            copy=state[:]
            copy[i],copy[j]=copy[j],copy[i]
            return copy

        while queue:
            new=[]
            for state in queue:
                if state==target:
                    return dist
                pos=state.index(0)
                for pos2 in moves[pos]:
                    new_state=swap(pos,pos2,state)
                    if tuple(new_state) not in visited:
                        new.append(new_state)
                        visited.add(tuple(new_state))
            queue=new
            dist+=1
        return -1

a=Solution()
print(a.slidingPuzzle([[1,2,3],[4,0,5]]))
print(a.slidingPuzzle([[1,2,3],[5,4,0]]))
print(a.slidingPuzzle([[4,1,2],[5,0,3]]))
print(a.slidingPuzzle([[3,2,4],[1,5,0]]))