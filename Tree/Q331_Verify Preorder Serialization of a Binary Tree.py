#       _9_
#      /   \
#     3     2
#    / \   / \
#   4   1  #  6
#  / \ / \   / \
#  # # # #   # #

# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true

# Input: "9,#,#,1"
# Output: false

# 两种思路
# Solution 1: 从底向上，每两个连续的#代表叶子节点，所以当出现两个连续#的时候，向上搜索，
# Solution 2: 从头到尾遍历输入,假设按照中序遍历的方式对节点进行挂载，那么每加入一个数字可挂载slot+1,，每加入一个'#'可挂载slot-1，在遍历过程中要一直保证slot>0，否则剩下的节点无法挂载，循环结束后slot需等于0

# Note:空节点提供的信息让重构二叉树变得可行

class Solution:

    # # Solution 1
    # def isValidSerialization(self, preorder):
    #     stack=[]
    #     for node in preorder.split(','):
    #         stack.append(node)
    #         while len(stack)>=3 and stack[-1]==stack[-2]=='#' and stack[-3]!='#':
    #             stack=stack[:-3]+['#']
    #     return stack==['#']

    # Solution 2
    def isValidSerialization(self, preorder):
        slot=1
        for node in preorder.split(','):
            if slot<=0: return False
            if node=='#': slot-=1
            else: slot+=1
        return slot==0


a=Solution()
print(a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(a.isValidSerialization("9,#,#,1"))