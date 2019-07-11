# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.

# 思路:1: 从后往前，记录当前的乘数
# 技巧1: 用ele和i处理多位组成的元素和下标的情况，如Mg13
# 技巧2: 从后往前方便找到当前应该乘的倍数
# 技巧3: 用stack存储每一层的乘数
# 技巧4: 用coff记录当前层的乘数coff，用n记录当前层的下标数

import collections
class Solution:
    def countOfAtoms(self, formula):
        c=collections.defaultdict(int)
        coff,n,i,stack,elem=1,0,0,[],''
        for char in formula[::-1]:
            if char.isdigit():
                n+=int(char)*(10**i)
                i+=1
            elif char==')':
                stack.append(n)
                coff*=n
                n,i=0,0
            elif char=='(':
                coff//=stack.pop()
            elif char.islower():
                elem+=char
            elif char.isupper():
                elem+=char
                c[elem[::-1]]+=(n or 1)*coff
                n,i,elem=0,0,''
        return ''.join(char+(n>1 and str(n) or '') for char,n in sorted(c.items()))

a=Solution()
print(a.countOfAtoms("K4(ON(SO3)2)2"))
print(a.countOfAtoms("Mg(OH)2"))