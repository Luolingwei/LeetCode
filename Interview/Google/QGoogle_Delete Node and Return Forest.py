
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:

    def delete(self, root: TreeNode, to_delete):
        to_delete = set(to_delete)
        self.res = []
        def dfs(node, parent_deleted):
            if not node: return None
            in_delet = node.val in to_delete
            if parent_deleted and not in_delet:
                self.res.append(node)
            new_children = []
            for child in node.children:
                if dfs(child, in_delet):
                    new_children.append(child)
            node.children = new_children
            return None if in_delet else node
        dfs(root, True)
        return self.res


    def construct(self, nums):
        memo = {}
        for child_val, parent_val in enumerate(nums):
            if parent_val==-1: continue
            if parent_val in memo: parent_node = memo[parent_val]
            else:
                parent_node = TreeNode(parent_val)
                memo[parent_val] = parent_node

            if child_val in memo: child_node = memo[child_val]
            else:
                child_node = TreeNode(child_val)
                memo[child_val] = child_node

            parent_node.children.append(child_node)
        return memo[0]


a=Solution()
root = a.construct([-1,0,0,1,1])
print(a.delete(root, [1,4]))