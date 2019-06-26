# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:
# TimeMap kv;
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
# kv.get("foo", 1);  // output "bar"
# kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // output "bar2"
# kv.get("foo", 5); //output "bar2"

# 题意: 初始化某个时间点的key-value对(后面可能还会加入另外时间点的key-value)，get的时候输入时间点(可能是以前的), 输出该时间点前面最近的value.

import bisect
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times=collections.defaultdict(list)
        self.values=collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx=bisect.bisect(self.times[key],timestamp)
        return self.values[key][idx-1] if idx>=1 else ''


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()

obj.set('love','high',10)
obj.set('love','low',20)
print(obj.get('love',5))
print(obj.get('love',10))
print(obj.get('love',15))