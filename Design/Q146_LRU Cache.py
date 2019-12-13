
# 思路: 用OrderedDict，每次put或者get之后将对应的key移动到末尾，size超出时，pop头部的item


import collections

# Solution 1 Doubly LinkedList
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.head = self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.nums = 0
        self.size = capacity
        self.key2node = {}

    def move_to_end(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.tail.pre.next
        node.pre = self.tail.pre
        node.next.pre = node.pre.next = node

    def delete_from_head(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        self.key2node.pop(node.key)

    def insert_to_end(self, node):
        node.next = self.tail.pre.next
        node.pre = self.tail.pre
        node.next.pre = node.pre.next = node

    def get(self, key):
        if key in self.key2node:
            curnode = self.key2node[key]
            self.move_to_end(curnode)
            return curnode.val
        else:
            return -1

    def put(self, key, value):
        if key in self.key2node:
            curnode = self.key2node[key]
            curnode.val = value
            self.move_to_end(curnode)
        else:
            newnode = Node(key, value)
            if self.nums == self.size:
                self.delete_from_head()
                self.nums -= 1
            self.insert_to_end(newnode)
            self.key2node[key] = newnode
            self.nums += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Solution 2 OrderedDict
# class LRUCache:
#     def __init__(self, capacity):
#         self.dic=collections.OrderedDict()
#         self.cap=capacity
#
#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]
#
#     def put(self, key, value):
#         self.dic[key]=value
#         self.dic.move_to_end(key)
#         if len(self.dic)>self.cap:
#             self.dic.popitem(last=False)


obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))