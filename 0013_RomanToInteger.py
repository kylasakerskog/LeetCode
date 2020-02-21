class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym_to_val = {"0":0, "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = s + "0"
        sum = 0
        for i in range(0,len(s)-1):
            if(sym_to_val[s[i]] >= sym_to_val[s[i+1]]):
                sum += sym_to_val[s[i]]
            else:
                sum -= sym_to_val[s[i]]
        return sum
