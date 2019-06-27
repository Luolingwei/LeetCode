import collections
class WordDictionary:

    # Solution 1 Tree
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.root = {}
    #
    # def addWord(self, word: str) -> None:
    #     """
    #     Adds a word into the data structure.
    #     """
    #     node = self.root
    #     for char in word:
    #         node = node.setdefault(char, {})
    #     node['$'] = None
    #
    # def search(self, word: str) -> bool:
    #     """
    #     Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    #     """
    #     nodes=[self.root]
    #     for char in word+'$':
    #         temp=[]
    #         for node in nodes:
    #             if char in node:
    #                 temp+=[node[char]]
    #             else:
    #                 if char=='.':
    #                     temp+=filter(None,node.values())
    #                 else:
    #                     temp+=[]
    #         nodes=temp
    #     return bool(nodes)

    # Solution 2 Classify by length
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map=collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.map[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        length=len(word)
        dic=self.map[length]
        if not dic:
            return False
        if '.' not in word:
            return word in dic
        for i in range(length):
            if word[i]=='.': continue
            dic={char for char in dic if char[i]==word[i]}
            if not dic:
                return False
        return True


a=WordDictionary()
print(a.addWord('at'))
print(a.addWord('and'))
print(a.addWord('an'))
print(a.addWord('add'))

print(a.search('a'))
print(a.search('at'))
print(a.search('bat'))
print(a.search('.at'))
print(a.search('a.d.'))
print(a.search('b.'))
print(a.search('a.d'))
print(a.search('.'))