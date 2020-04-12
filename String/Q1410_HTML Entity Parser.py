
# 根据替换规则从前往后replace即可

class Solution:
    def entityParser(self, text: str) -> str:
        i=0
        res=''
        while i<len(text):
            c=text[i]
            if c=='&':
                if text[i:i+6] == '&quot;':
                    i+=6
                    res+='"'
                elif text[i:i+6] == '&apos;':
                    i+=6
                    res+="'"
                elif text[i:i+5] == '&amp;':
                    i+=5
                    res+="&"
                elif text[i:i+4] == '&gt;':
                    i+=4
                    res+=">"
                elif text[i:i+4] == '&lt;':
                    i+=4
                    res+="<"
                elif text[i:i+7] == '&frasl;':
                    i+=7
                    res+="/"
                else:
                    res+='&'
                    i+=1
            else:
                res+=c
                i+=1
        return res