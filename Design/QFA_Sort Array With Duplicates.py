class TreeNode:
    def __init__(self,x):
        self.val=x
        self.count=1
        self.left=None
        self.right=None

class Build:

    def __init__(self):
        self.root=None
        self.ans=[]

    def insert(self,i):
        if not self.root:
            self.root=TreeNode(i)
        else:
            node=self.root
            while node:
                if node.val==i:
                    node.count+=1
                    break
                elif node.val>i:
                    if not node.left:
                        node.left=TreeNode(i)
                        break
                    node=node.left
                else:
                    if not node.right:
                        node.right=TreeNode(i)
                        break
                    node=node.right

    def frequency(self,j):
        node=self.root
        while node:
            if node.val==j:
                return node.count
            elif node.val>j:
                node=node.left
            else:
                node=node.right
        return 0

    def sort(self,nums):
        for n in nums:
            self.insert(n)
        def inorder(node):
            if node:
                inorder(node.left)
                self.ans+=[node.val]*node.count
                inorder(node.right)
        inorder(self.root)
        return self.ans

a=Build()
# print(a.sort(['v','c','c','a','a','b','b','b','b','b','a','a']))
print(a.sort(["abc","ab","dea","ca","bbb","ab","wrs","abd","abc","kis"]))
# a.insert(2)
# a.insert(2)
# a.insert(6)
# a.insert(6)
# print(a.frequency(3))
# print(a.frequency(2))
# print(a.frequency(6))