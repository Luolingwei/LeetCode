
# 思路: 统计空格个数, 筛除words, 然后join

class Solution:
    def reorderSpaces(self, text: str) -> str:
        empty = text.count(' ')
        words = text.split()
        if len(words) == 1: return words[0] + ' ' * empty
        spaceN, left = divmod(empty, len(words) - 1)
        res = (' ' * spaceN).join(words)
        return res + ' ' * left

a=Solution()
print(a.reorderSpaces("  this   is  a sentence "))
print(a.reorderSpaces(" practice   makes   perfect"))
print(a.reorderSpaces("hello   world"))
print(a.reorderSpaces("a"))