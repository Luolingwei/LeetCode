# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation:
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
#
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.

# 思路: 单调栈，每来一个大数，pop出stack中比它小的，加上它们各自carry的数字个数，并把当前数也入栈
# stack中的数单调递减，每个数字carry的是前面比它们小的个数，如果当前数n大于stack[-1]，那么它比carry的数都大，否则以carry==1加入栈尾

class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        ans=1
        while self.stack and price>=self.stack[-1][0]:
            ans+=self.stack.pop()[1]
        self.stack.append((price,ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))