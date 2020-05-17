
# 思路: 将split之后的word根据len排序, capitalize函数将字符串的第一个字母变成大写,其他字母变小写

class Solution:
    def arrangeWords(self, text: str) -> str:
        return ' '.join(sorted(text.split(),key=len)).capitalize()