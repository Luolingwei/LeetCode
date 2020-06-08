class BrowserHistory:

    def __init__(self, homepage: str):
        self.memo = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.memo = self.memo[:self.pos+1]
        self.memo.append(url)
        self.pos = len(self.memo)-1

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos-steps)
        return self.memo[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.memo)-1, self.pos+steps)
        return self.memo[self.pos]


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