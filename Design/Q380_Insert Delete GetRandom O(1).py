
# 思路: 建立一个array存所有数字，一个hashmap建立val和index的映射
# insert的时候直接加入array末尾，更新map.
# delete的时候把val和数组末尾数字交换，然后pop(pop(i)为O(n))，同时更新map

import random
class RandomizedSet:

    def __init__(self):
        self.map={}
        self.array=[]
        self.length=0

    def insert(self, val):
        if val in self.map:
            return False
        else:
            self.array.append(val)
            self.length+=1
            self.map[val]=self.length-1
            return True

    def remove(self, val):
        if val in self.map:
            idx=self.map[val]
            last=self.array[-1]
            self.array[idx],self.array[self.length-1]=self.array[self.length-1],self.array[idx]
            self.map[last]=idx
            del self.map[val]
            self.array.pop()
            self.length-=1
            return True
        else:
            return False

    def getRandom(self):
        return self.array[random.randint(0,self.length-1)]


obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(1))
print(obj.insert(3))
print(obj.remove(4))
print(obj.getRandom())
print(obj.getRandom())
print(obj.remove(2))
print(obj.getRandom())
print(obj.getRandom())