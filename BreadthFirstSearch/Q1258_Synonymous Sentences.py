
# 思路: 先构建相互替换的graph，bfs每次替换一个word，注意不要回访.

import collections
class Solution:
    def generateSentences(self, synonyms, text):
        graph = collections.defaultdict(dict)
        bfs = collections.deque()
        ans = set()
        bfs.append(text)
        for k, v in synonyms:
            graph[k][v] = 1
            graph[v][k] = 1
        while bfs:
            curT = bfs.popleft()
            ans.add(curT)
            words = curT.split()
            for i, w in enumerate(words):
                if w in graph.keys():
                    for newW in graph[w]:
                        newsent = ' '.join(words[:i] + [newW] + words[i + 1:])
                        if newsent not in ans:
                            bfs.append(newsent)
        return sorted(list(ans))

a=Solution()
print(a.generateSentences([["happy","joy"],["sad","sorrow"],["joy","cheerful"]],"I am happy today but was sad yesterday"))