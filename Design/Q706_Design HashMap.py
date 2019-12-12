'''
use array+LinkedList to design Hashmap, calculate Hashcode for each key.
'''


class ListNode:
    def __init__(self,key,val):
        self.pair=(key,val)
        self.next=None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arrayL=1000
        self.array=[None]*self.arrayL

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        slot=key%self.arrayL
        if not self.array[slot]:
            self.array[slot]=ListNode(key,value)
        else:
            curnode=self.array[slot]
            while curnode:
                if curnode.pair[0]==key:
                    curnode.pair=(key,value)
                    return
                if curnode.next==None: break
                curnode=curnode.next
            curnode.next=ListNode(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        slot=key%self.arrayL
        curnode=self.array[slot]
        while curnode:
            if curnode.pair[0]==key:
                return curnode.pair[1]
            curnode=curnode.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        slot=key%self.arrayL
        pre=cur=self.array[slot]
        if not cur: return
        if cur.pair[0]==key:
            self.array[slot]=cur.next
        else:
            cur=cur.next
            while cur:
                if cur.pair[0]==key:
                    pre.next=cur.next
                    return
                pre,cur=pre.next,cur.next

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))