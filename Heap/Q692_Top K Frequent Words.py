# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.

# 思路 1: 用 Counter记录出现次数并排序
# 思路 2: 用 heap 记录 freq和word，并依次pop出k个

import collections
import heapq
class Solution:
    # Solution 1 Counter
    # def topKFrequent(self, words, k):
    #     dic=collections.Counter(words)
    #     return sorted(dic,key=lambda x: (-dic[x],x))[:k]

    # Solution 2 Heap
    def topKFrequent(self, words, k):
        dic,queue=collections.Counter(words),[]
        for word, freq in dic.items():
            heapq.heappush(queue,(-freq,word))
        return [heapq.heappop(queue)[1] for _ in range(k)]

a=Solution()
print(a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))
print(a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))