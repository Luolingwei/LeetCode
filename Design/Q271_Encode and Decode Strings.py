
# 思路1: 将'|'替换为'||'，然后用' | '进行分隔，' | '不会出现在原string中. decode时用' | 'split然后替换回来即可
# 思路2: 将字符串的长度信息加在字符串头部进行encode，就知道从什么位置进行分割了

class Codec:

    # Solution 1
    # def encode(self, strs):
    #     """Encodes a list of strings to a single string.
    #     """
    #     return ''.join([s.replace('|', '||') + ' | ' for s in strs])
    #
    # def decode(self, s):
    #     """Decodes a single string to a list of strings.
    #     """
    #     return [c.replace('||', '|') for c in s.split(' | ')[:-1]]

    # Solution 2
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        return ''.join([str(len(s))+':'+s for s in strs])

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        i,N=0,len(s)
        res=[]
        while i<N:
            idx=s.find(':',i)
            res.append(s[idx+1:idx+1+int(s[i:idx])])
            i=idx+1+int(s[i:idx])
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))