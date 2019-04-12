class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for char in word:
            node=node.setdefault(char,{})
        node['$']=None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nodes=[self.root]
        for char in word+'$':
            temp=[]
            for node in nodes:
                if char in node:
                    temp+=[node[char]]
            nodes=temp
        return bool(nodes)


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nodes=[self.root]
        for char in prefix:
            temp=[]
            for node in nodes:
                if char in node:
                    temp+=[node[char]]
            nodes=temp
        return bool(nodes)


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))


