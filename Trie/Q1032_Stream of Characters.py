
# 思路: 先建立前缀树, 然后每次碰到一个新letter, 对node list里面的node进行下一层更新, 如果有letter则跳到下一层
# 检查是否有结束符 '$'出现

class StreamChecker:

    def __init__(self, words):
        self.root = {}
        self.nodes = []
        for word in words:
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = None

    def query(self, letter: str) -> bool:
        new_nodes = []
        for node in self.nodes:
            if letter in node:
                new_nodes.append(node[letter])
        if letter in self.root:
            new_nodes.append(self.root[letter])
        self.nodes = new_nodes
        return any('$' in node for node in self.nodes)


a=StreamChecker(["cd","f","kl"])
print(a.query('a'))
print(a.query('b'))
print(a.query('c'))
print(a.query('d'))
print(a.query('e'))
print(a.query('f'))
print(a.query('g'))
print(a.query('h'))
print(a.query('i'))
print(a.query('j'))
print(a.query('k'))
print(a.query('l'))