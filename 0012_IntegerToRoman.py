# 12. Integer to Roman
"""
Runtime: 48 ms, faster than 67.59% of Python3 online submissions for Integer to Roman.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        romanInt = {1000 : 'M',
                    900 : 'CM',
                    500 : 'D',
                    400 : 'CD',
                    100 : 'C',
                    90 : 'XC',
                    50 : 'L',
                    40 : 'XL',
                    10 : 'X',
                    9 : 'IX',
                    5 : 'V',
                    4 : 'IV',
                    1 : 'I'}
        roman = ""
        for key in romanInt:
            while num >= key:
                num -= key
                roman += romanInt[key]
                
        return roman
