# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

# 思路: 用正则匹配所有小写的单词，然后用Counter找出不在banned中的最高频单词.

import re
import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        ban=set(banned)
        strs=re.findall("\w+",paragraph.lower())
        return collections.Counter(filter(lambda c:c not in ban,strs)).most_common(1)[0][0]

a=Solution()
print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))