# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.

# 思路 1: 用 Counter记录出现次数并排序
# 思路 2: 用 heap 记录 freq和word，并依次pop出k个

import collections
import heapq
class Solution:
    # Solution 1 Counter O(nlogn)
    # def topKFrequent(self, words, k):
    #     dic=collections.Counter(words)
    #     return sorted(dic,key=lambda x: (-dic[x],x))[:k]

    # Solution 2 Heap O(klogn)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        q = [(-n, word) for word, n in count.items()]
        heapq.heapify(q)
        return [heapq.heappop(q)[1] for _ in range(k)]

a=Solution()
print(a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2))
print(a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))