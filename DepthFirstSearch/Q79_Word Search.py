# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

# 思路: 此题的不同之处在于，需要给每一个路径单独设置visit，不同路径之间是可以重复访问的，而同一条路径上不可以回访。
# 这里就用visited记录每条路径的节点(i,j)，防止回访，但是如果某条路径没有找到ans的话，需要回溯，即visited.remove((i,j))，使节点可以被其他路径使用。

class Solution:
    def exist(self, board, word):
        if not board: return False
        m,n=len(board),len(board[0])
        target,visited=len(word),set()
        def dfs(i,j,pos,target):
            nonlocal m,n,visited
            if pos==target:
                return True
            if 0<=i<m and 0<=j<n and board[i][j]==word[pos] and (i,j) not in visited:
                visited.add((i,j))
                if dfs(i+1,j,pos+1,target) or dfs(i-1,j,pos+1,target) or dfs(i,j+1,pos+1,target) or dfs(i,j-1,pos+1,target):
                    return True
                visited.remove((i,j)) # backtracking, 如果没有找到答案的话，(i,j)仍然可以被其他路径使用
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0,target):
                    return True
        return False

a=Solution()
print(a.exist([
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
],"ABCCED"))
print(a.exist([
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
],"SEE"))
print(a.exist([
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
],"ABCB"))
print(a.exist([
["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]
],"ABCESEEEFS"))

print(a.exist([[]],"ABCESEEEFS"))