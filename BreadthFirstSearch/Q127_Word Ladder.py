# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0

# 思路: 用一个队列存储每一轮替换（每轮只替换一个字母）的结果，上一轮的字符串pop完之后才会pop下一轮的，所以一旦找到endword，就返回distance，一定是最短路径

class Solution:
    # Solution 1 Time Limit Exceeded
    # def ladderLength(self, beginWord, endWord, wordList):
    #     def bfs(beginWord, endWord, wordList):
    #         length=float('inf')
    #         for i in range(len(beginWord)):
    #             for char in 'abcdefghijklmnopqrstuvwxyz':
    #                 for j in range(len(wordList)):
    #                     if beginWord[:i]+char+beginWord[i+1:]==endWord==wordList[j]:
    #                         return 2
    #                     elif beginWord[:i]+char+beginWord[i+1:]==wordList[j]:
    #                         length=min(length,bfs(beginWord[:i]+char+beginWord[i+1:],endWord,wordList[:j]+wordList[j+1:])+1)
    #         return length
    #
    #     ans=bfs(beginWord,endWord,wordList)
    #     return 0 if ans==float('inf') else ans
    #     return ans

    # Solution 2
    def ladderLength(self, beginWord, endWord, wordList):
        queue=[(beginWord,1)]
        wordList=set(wordList)
        visited=set()

        while queue:
            word,distance=queue.pop(0)
            if word==endWord:
                return distance
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    temp=word[:i]+char+word[i+1:]
                    if temp in wordList and temp not in visited: # 防止往回访问 如dot->dog->dot:
                        queue.append((temp,distance+1))
                        visited.add(temp)
        return 0


a=Solution()
print(a.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(a.ladderLength("hit","cog",["hot","dot","dog","lot","log"]))
print(a.ladderLength("hot","dog",["hot","dog","dot"]))