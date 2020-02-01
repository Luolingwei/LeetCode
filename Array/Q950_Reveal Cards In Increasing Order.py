
# 思路: 模拟pop和reverse的逆过程，每次把最后一个元素拿到第一个，并在开头放置下一个元素（从大到小）

class Solution:
    def deckRevealedIncreasing(self, deck):
        q=[]
        for i in sorted(deck)[::-1]:
            q=[i]+q[-1:]+q[:-1]
        return q

a=Solution()
print(a.deckRevealedIncreasing([17,13,11,2,3,5,7]))