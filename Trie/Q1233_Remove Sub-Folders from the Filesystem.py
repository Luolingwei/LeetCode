
# 思路: 建立path的前缀树，一层一层往下搜索，碰到$时，此路径终止向下，将node['$']加入ans，其子路径将不会被搜索.

class Solution:
    def removeSubfolders(self, folder):
        self.root = {}
        self.ans = []

        def insert(path):
            node = self.root
            for char in path.split('/'):
                node = node.setdefault(char, {})
            if '$' in node:
                node['$'].append(path)
            node['$'] = [path]

        def search():
            nodes = [self.root]
            while nodes:
                temp = []
                for node in nodes:
                    if '$' in node:
                        self.ans+=node['$']
                    else:
                        temp+=[d for d in node.values()]
                nodes = temp

        for path in folder:
            insert(path)
        search()
        return self.ans

a=Solution()
print(a.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(a.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
print(a.removeSubfolders(["/a","/a/b/c","/a/b/d"]))