# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.

# 思路: 用dic存储curS，遇到相同的curS删除中间一段，始终储存最先出现的curS的节点

class Solution:
    def removeZeroSumSublists(self, head):
        prehead=ListNode(0)
        prehead.next=head
        S,p,curS={},prehead,0
        while p:
            curS+=p.val
            if curS in S:
                S[curS].next=p.next
            else:
                S[curS]=p
            p=p.next
        return prehead.next