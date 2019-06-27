# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# 思路: 前缀树方法.

class Solution:
    def __init__(self):
        self.root={}

    def insert(self,word):
        node=self.root
        for char in word:
            node=node.setdefault(char,{})
        node['$']=None

    def search(self,word):
        nodes=[self.root]
        for i in range(len(word)):
            temp=[]
            for node in nodes:
                if '$' in node:
                    return word[:i]
                if word[i] in node:
                    temp+=[node[word[i]]]
            nodes=temp
        return word

    def replaceWords(self, dict, sentence):
        for root in dict:
            self.insert(root)
        return ' '.join(map(self.search,sentence.split()))

a=Solution()
print(a.replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery"))