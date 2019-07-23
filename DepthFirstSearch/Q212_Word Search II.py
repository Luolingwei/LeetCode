# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]

# 思路: 不同于word search I, 这里有多个word，可能出现相同的前缀，所以将整个words集合转成Trie存储，可减少相同字母的搜索次数
# 如: {"air", "aisle"} 其中的ai就都只需要dfs一次，如果没有trie需要分别dfs(因为它们是两个word)

class Solution:
    def findWords(self, board, words):
        m,n,ans=len(board),len(board) and len(board[0]),set()
        Trie={}
        for word in words:
            node=Trie
            for c in word:
                node=node.setdefault(c,{})
            node['$']=None

        def dfs(i,j,word,node,visited):
            if 0<=i<m and 0<=j<n and (i,j) not in visited:
                if board[i][j] in node:
                    node,word=node[board[i][j]],word+board[i][j]
                    if '$' in node: ans.add(word)
                    visited.add((i,j))
                    dfs(i+1,j,word,node,visited)
                    dfs(i-1,j,word,node,visited)
                    dfs(i,j-1,word,node,visited)
                    dfs(i,j+1,word,node,visited)
                    visited.remove((i,j))

        for i in range(m):
            for j in range(n):
                dfs(i,j,'',Trie,set())

        return list(ans)

a=Solution()
print(a.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"]))