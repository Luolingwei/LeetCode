
# 思路: 建立一个array存所有数字，一个hashmap建立val和index的映射，因为有重复值，这里val->set(indexes)
# insert的时候直接加入array末尾，更新map.
# delete的时候把pop一个val的index,把val和数组末尾数字交换，然后pop数组，同时更新map

import collections
import random
class RandomizedCollection:

    def __init__(self):
        self.map=collections.defaultdict(set)
        self.array=[]
        self.length=0

    def insert(self, val):
        def update(val):
            self.array.append(val)
            self.length+=1
            self.map[val].add(self.length-1)
        if val in self.map:
            update(val)
            return False
        else:
            update(val)
            return True

    def remove(self, val):
        if self.map[val]:
            idx=self.map[val].pop()
            last=self.array[-1]
            self.array[idx],self.array[self.length-1]=self.array[self.length-1],self.array[idx]
            if self.map[last]:
                self.map[last].discard(self.length-1)
                self.map[last].add(idx)
            self.array.pop()
            self.length-=1
            return True
        else:
            return False

    def getRandom(self):
        return self.array[random.randint(0,self.length-1)]

obj = RandomizedCollection()
print(obj.insert(0))
print(obj.remove(0))
print(obj.insert(-1))
print(obj.remove(0))
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())