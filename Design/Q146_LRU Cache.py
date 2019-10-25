
# 思路: 用OrderedDict，每次put或者get之后将对应的key移动到末尾，size超出时，pop头部的item

import collections
class LRUCache:

    def __init__(self, capacity):
        self.dic=collections.OrderedDict()
        self.cap=capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key, value):
        self.dic[key]=value
        self.dic.move_to_end(key)
        if len(self.dic)>self.cap:
            self.dic.popitem(last=False)


obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))