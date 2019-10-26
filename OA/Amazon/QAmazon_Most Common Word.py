import re
import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        strs=re.split('[^a-z]+',paragraph.lower())
        ban=set(banned)
        return collections.Counter(w for w in strs if w not in ban).most_common()[0][0]

a=Solution()
print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))