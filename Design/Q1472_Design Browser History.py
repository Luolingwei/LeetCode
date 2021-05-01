
# 思路: 记录当前位置进行前后移动, visit新page时， 将tail设置成下一个位置, 而不需要清空后面的所有记录, 重写复用即可

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0
        self.tail = 0

    def visit(self, url: str) -> None:
        self.tail = self.pos+1
        if self.tail==len(self.history):
            self.history.append(url)
        else:
            self.history[self.tail] = url
        self.pos = self.tail

    def back(self, steps: int) -> str:
        self.pos = max(0,self.pos-steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.tail,self.pos+steps)
        return self.history[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin.com")
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))