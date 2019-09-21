# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

# 思路: 用前缀树建立value的索引，sum的时候搜索后面所有的value加起来

class MapSum:

    def __init__(self):
        self.root={}

    def insert(self, key, val):
        node=self.root
        for c in key:
            node=node.setdefault(c,{})
        node['$']=val

    def sum(self, prefix):
        nodes=[self.root]
        s=0
        for c in prefix:
            temp=[]
            for node in nodes:
                if c in node:
                    temp+=[node[c]]
            nodes=temp

        while nodes:
            temp=[]
            for node in nodes:
                for key in node:
                    if key=='$':
                        s+=node['$']
                    else:
                        temp+=[node[key]]
            nodes=temp
        return s

a=MapSum()
a.insert("apple",3)
print(a.sum("ap"))
a.insert("app",2)
print(a.sum("ap"))