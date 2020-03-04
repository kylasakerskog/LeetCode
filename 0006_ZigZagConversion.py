"""
Runtime: 52 ms, faster than 86.74% of Python3 online submissions for ZigZag Conversion.  
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.  
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;
        cycle =	2 * numRows - 2
        slist = ""
        s_len = len(s)
        for i in range(numRows):
            for j in range(i, s_len, cycle):
                slist += s[j]
                if i != 0 and i != numRows - 1:
                    btw = j + 2*(numRows-i-1)
                    if btw < s_len:
                        slist += s[btw]        
        return slist
