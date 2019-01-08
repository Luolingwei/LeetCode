class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        digits = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return thousands[num//1000%10]+hundreds[num//100%10]+tens[num//10%10]+digits[num%10]

a=Solution()
print(a.intToRoman(1994))