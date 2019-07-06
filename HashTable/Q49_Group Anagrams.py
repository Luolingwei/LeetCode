# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# 思路: 用字典存储同一个group的单词.

import collections
class Solution:
    def groupAnagrams(self, strs):
        memo=collections.defaultdict(list)
        for char in strs:
            key=''.join(sorted(char))
            memo[key].append(char)
        return list(memo.values())

a=Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "eat", "nat", "tan"]))