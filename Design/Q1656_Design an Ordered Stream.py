
# 思路: 直接模拟, 设置初始ptr在1的位置, 每次插入, 然后移动ptr直到空为止

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""]*(n+2)
        self.idx = 1

    def insert(self, id: int, value: str):
        self.stream[id] = value
        preIdx = self.idx
        while self.stream[self.idx]:
            self.idx+=1
        return self.stream[preIdx:self.idx]


os= OrderedStream(5)
print(os.insert(3, "ccccc")) # Inserts (3, "ccccc"), returns [].
print(os.insert(1, "aaaaa")) # Inserts (1, "aaaaa"), returns ["aaaaa"].
print(os.insert(2, "bbbbb")) # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
print(os.insert(5, "eeeee")) # Inserts (5, "eeeee"), returns [].
print(os.insert(4, "ddddd")) # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].